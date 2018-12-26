import atexit
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import DesiredCapabilities
from urllib3.exceptions import MaxRetryError

from Tools.BrowserStack import BrowserStack
from Tools.ConfigManager import ConfigManager

_instance = None

def init_chrome():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = "/usr/bin/chromium-browser"
    chrome_options.add_argument('--no-proxy-server')
    chrome_options.add_argument('--disable-gpu')
    if ConfigManager["Default"].multiple_monitors:
        pos = f'--window-position={ConfigManager["Default"].window_x},{ConfigManager["Default"].window_y}'
        chrome_options.add_argument(pos)
    chrome_options.add_argument('--window-size=1312,754')
    return webdriver.Chrome(chrome_options=chrome_options)

def init_firefox():
    firefox_options = webdriver.FirefoxOptions()
    # chrome_options.binary_location = "/usr/bin/chromium-browser"
    firefox_options.add_argument('--no-proxy-server')
    firefox_options.add_argument('--disable-gpu')
    if ConfigManager["Default"].multiple_monitors:
        pos = f'--window-position={ConfigManager["Default"].window_x},{ConfigManager["Default"].window_y}'
        firefox_options.add_argument(pos)
    firefox_options.add_argument('--window-size=1312,754')
    return webdriver.Firefox(firefox_options=firefox_options)

def init_remote():
    dc = BrowserStack.get_config("Default")
    desired_capabilities = {}
    if dc["browser"] == "firefox":
        desired_capabilities = DesiredCapabilities.FIREFOX.copy()
    if dc["browser"] == "chrome":
        desired_capabilities = DesiredCapabilities.CHROME.copy()
    desired_capabilities.update(dc)
    # capabilities['platform'] = "MAC"
    return webdriver.Remote(desired_capabilities=desired_capabilities, command_executor='http://172.17.0.1:4444/wd/hub')

def create_instance():
    if ConfigManager["Default"].remote_testing:
        res = init_remote()
    elif BrowserStack["browser"].lower() == "chrome":
        res = init_chrome()
    elif BrowserStack["browser"].lower() == "firefox":
        res = init_firefox()
    else:
        raise Exception("Selected browser not recognized ({})".format(BrowserStack["browser"]))

    if not ConfigManager["Default"].remote_testing:
        if ConfigManager["Default"].implicitwait > 0:
            res.implicitly_wait(ConfigManager["Default"].implicitwait_timeout)
    if ConfigManager["Default"].maximize:
        res.maximize_window()
        # pyautogui.hotkey('shift', 'winleft', 'right')
        # pyautogui.hotkey('shift', 'winleft', 'right')

    # res.set_page_load_timeout(ConfigManager["Default"].pageload)

    def ex():
        try:
            res.close()
        except WebDriverException:
            pass
        except MaxRetryError:
            pass

    atexit.register(ex)

    return res

class Driver(object):

    def __get__(self, instance, owner):
        global _instance
        if _instance is None:
            _instance = create_instance()
        return _instance

    def __set__(self, instance, value):
        raise NotImplementedError()

    @staticmethod
    def quit():
        global _instance
        if _instance is not None:
            _instance.quit()
            time.sleep(10)
            _instance = None

import atexit
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from urllib3.exceptions import MaxRetryError

from web.enums import Browser

_instance = None

def init_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-proxy-server')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1312,754')
    return webdriver.Chrome(chrome_options=chrome_options)

def init_firefox():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--no-proxy-server')
    firefox_options.add_argument('--disable-gpu')
    firefox_options.add_argument('--window-size=1312,754')
    return webdriver.Firefox(firefox_options=firefox_options)

def create_instance(browser:Browser):
    if browser == Browser.Chrome:
        res = init_chrome()
    elif browser == Browser.Firefox:
        res = init_firefox()
    else:
        raise Exception(f"Selected browser not recognized ({browser})")

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

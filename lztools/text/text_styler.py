
"""
import time

from requests_html import HTMLSession

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import asyncio
from pyppeteer import launch
import pyppeteer
from bash import command

def rainbow(text, frequency=0.1, hide_gap=True):
    if frequency is None:
        frequency = 0.1
    args = ["--freq", str(frequency)]

    m = "| sed '$d' " if hide_gap else ""
    argsd = str.join(" ", args)

    return command(f"echo \"{text}\" {m}| lolcat -f {argsd} 2> /dev/null", return_result=True)

pyppeteer.launch()
async def main():
    browser = await launch()
    page = await browser.newPage()
    page
    page.go
    await page.goto('http://example.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

TEXT_STYLE_MIN = 1
TEXT_STYLE_MAX = 16

DECORATION_STYLE_MIN = 1
DECORATION_STYLE_MAX = 37

_url = "http://www.webestools.com/stylish-text-generator-nickname-message-msn-facebook-windows-live-messenger-text-accents-effect-ascii-text.html"

sesh = HTMLSession()

resp = sesh.post(_url, params={"textEffect": False, "textEffectStyle": 5, "decorationStyle": 34, "lztext": "kaskelot", "decoration":False})
resp.hrml.render()

print("kaskelot" in resp)
phtml = BeautifulSoup(resp.text)
i = phtml.body.find("input")
print(i)
# return
for part in resp.text.split("preview"):
    print(part[:200])
    time.sleep(1)
# return resp
"""
from requests_html import HTMLSession

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import asyncio
from pyppeteer import launch
import pyppeteer
pyppeteer.launch()

async def main():
    browser = await launch()
    page = await browser.newPage()
    page.
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

resp = sesh.post(_url, params={"textEffect": False, "textEffectStyle": 5, "decorationStyle": 34, "text": "kaskelot", "decoration":False})
resp.hrml.render()

print("kaskelot" in resp)
phtml = BeautifulSoup(resp.text)
i = phtml.body.find("input")
print(i)
return
for part in resp.text.split("preview"):
    print(part[:200])
    time.sleep(1)
return resp
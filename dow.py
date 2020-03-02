import urllib.request
import ssl
from bs4 import BeautifulSoup

url = "https://finance.yahoo.co.jp/quote/%5EDJI"

ssl._create_default_https_context = ssl._create_unverified_context

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

p = soup.find_all("p")

dow = ""
for tag in p:
    try:
        string_ = tag.get("class").pop(0)

        if string_ in "wlbmIy9W":
            dow = tag.string
            break
    except:
        pass

print(dow)

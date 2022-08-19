import os
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://www.todaytvseries1.com/tv-series/612-evil-cbs")

if response.status_code == 200:
    data = response.content.decode()
    soup = BeautifulSoup(data, "html.parser")
    urls = []

    for a in soup.find_all('a', href=True):
        if "EVL10" in a['href']:
            urls.append(a['href'])

    urls.reverse()
    portion = urls[0:10]

    for key in portion:
        target_file = key.replace(
            "http://tirnaice2th.parsaspace.com/un5gjct7qe8cgqwuecgiecohovq/", "")
        os.system(f"mkdir evil && cd evil")
        try:
            os.system(f"wget {key}")
        except Exception as e:
            print(e)
            break

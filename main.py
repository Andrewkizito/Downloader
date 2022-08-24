import os
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://www.todaytvseries1.com/tv-series/210-better-call-saul-tv1")

if response.status_code == 200:
    data = response.content.decode()
    soup = BeautifulSoup(data, "html.parser")
    urls = []

    for a in soup.find_all('a', href=True):
        if "Btr.C.S.S03E" in a['href']:
            urls.append(a['href'])

    urls.reverse()
    portion = urls[1:10]
    print(portion)

    # for key in portion:
    #     target_file = key.replace(
    #         "http://tirnaice2th.parsaspace.com/un5gjct7qe8cgqwuecgiecohovq/", "")
    #     os.system(f"mkdir evil && cd evil")
    #     try:
    #         os.system(f"wget {key}")
    #     except Exception as e:
    #         print(e)
    #         break

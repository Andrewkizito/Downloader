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
        if "Btr.C.S.S04E" in a['href']:
            urls.append(a['href'])

    urls.reverse()
    portion = urls[0:10]
    print(portion)

    os.system(f"mkdir bcs && cd bcs")
    for key in portion:
        target_file = key.replace(
            "http://transfer1.parsaspace.com/yvhkvh0q2g7uohuklvh8oplfvbyigv79q2goehkgv7oug/", "")
        try:
            os.system(f"wget {key}")
        except Exception as e:
            print(e)
            break

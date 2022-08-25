import os
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://www.todaytvseries1.com/tv-series/323-stranger-things-netflix-tv")

if response.status_code == 200:
    data = response.content.decode()
    soup = BeautifulSoup(data, "html.parser")
    urls = []

    for a in soup.find_all('a', href=True):
        if "S01E0" in a['href']:
            urls.append(a['href'])

    urls.reverse()
    portion = urls[4:8]
    print(portion)

    for key in portion:
        try:
            os.system(f"wget {key}")
        except Exception as e:
            print(e)
            break

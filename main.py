#!/usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://www.todaytvseries2.com/tv-series/210-better-call-saul-tv1"
)

if response.status_code == 200:
    data = response.content.decode()
    soup = BeautifulSoup(data, "html.parser")

urls = []
for a in soup.find_all("a", href=True):
    if "Btr.C.S.S06" in a["href"]:
        urls.append(a["href"])

urls.reverse()
keys = urls[:6]


for key in keys:
    os.system(f"wget {key}")

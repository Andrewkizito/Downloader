#!/usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://www.todaytvseries2.com/tv-series/85-the-walking-dead-tv"
)

if response.status_code == 200:
    data = response.content.decode()
    soup = BeautifulSoup(data, "html.parser")

urls = []
for a in soup.find_all("a", href=True):
    if "The.Wlk.Ded.S05" in a["href"]:
        urls.append(a["href"])

urls.reverse()
keys = urls

for key in keys:
    os.system(f"wget {key}")

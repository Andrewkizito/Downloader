#!/usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://www.todaytvseries2.com/tv-series/190-colony-tv1")

if response.status_code == 200:
    data = response.content.decode()
    soup = BeautifulSoup(data, "html.parser")

urls = []
for a in soup.find_all('a', href=True):
    if "S05" in a['href'] or "Cly.S01E0" in a['href']:
        urls.append(a['href'])

print(urls)

for key in urls:
    os.system(f"wget {key}")

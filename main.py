#!/usr/bin/python3
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
    if "S05" in a['href'] or "BtrCS.5E" in a['href']:
        urls.append(a['href'])

print(urls)

os.system("mkdir files")
os.system("cd files")

for key in urls:
    os.system(f"wget {key}")

#!/usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://www.todaytvseries1.com/tv-series/685-house-of-the-dragon-hbo-max")

if response.status_code == 200:
    data = response.content.decode()
    soup = BeautifulSoup(data, "html.parser")

urls = []
for a in soup.find_all('a', href=True):
    if "S04E0" in a['href']:
        urls.append(a['href'])

        urls.reverse()
        portion = urls[0:9]

os.system("mkdir files")
os.system("cd files")

for key in urls:
    os.system(f"wget {key}")

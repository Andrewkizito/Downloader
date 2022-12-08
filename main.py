#!/usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "http://www.todaytvseries2.com/tv-series/85-the-walking-dead-tv")

if response.status_code == 200:
    data = response.content.decode()
    soup = BeautifulSoup(data, "html.parser")

urls = []
for a in soup.find_all('a', href=True):
    if "The.Wlk.Ded.S01E" in a['href']:
        urls.append(a['href'])

my_urls = urls.reverse()

os.system("mkdir ~/the-100")
os.system("cd ~/the-100")

for key in urls:
    os.system(f"wget {key}")

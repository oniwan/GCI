#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import commands
import requests
import time
from bs4 import BeautifulSoup

BASE_URL = u"http://www.management.e.u-tokyo.ac.jp/lecture/qf1_2017/"
EXTENSION = u"pdf"

urls = [
    u"http://www.management.e.u-tokyo.ac.jp/lecture/qf1_2017/",
]

for url in urls:
    download_urls = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    links = soup.findAll('a')

    # Extract Url
    for link in links:
        href = link.get('href')
        if href and EXTENSION in href:
            download_urls.append(href)

    # Download
    for download_url in download_urls:

        # Sleep one second
        # time.sleep(1)

        file_name = download_url.split("/")[-1]

        if BASE_URL in download_url:
            r = requests.get(download_url)
        else:
            r = requests.get(BASE_URL + download_url)

        # Save File
        if r.status_code == 200:
            f = open(file_name, 'w')
            f.write(r.content)
            f.close()

directory = "/home/kazuki"
pdflist = os.listdir(directory)
print pdflist
pdflist2 = []
regex = r"(pdf)$"
for y in pdflist:
    match = re.search(regex, y)
    if match:
        pdflist2.append(y)
print pdflist2

cnt = 0
for x in pdflist2:
    path = os.path.join(directory, x)
    print
    name = 'PDF%04d' % cnt + '.txt'
    os.system("pdf2txt.py" + " -o " + name + " " + path)
    cnt += 1

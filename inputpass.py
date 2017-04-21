#! usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import re
import commands
import requests
import time
from bs4 import BeautifulSoup
import mechanize

br = mechanize.Browser()
# Setting url,account,password,browser
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
url = "https://lzone.daiwa.co.jp/lzone/common/authorize"
username='shinichiro.ueno@gci.jp'
password = 'gcigci'

# Open and Submit password
response = br.open(url)
#print response.read()
br.select_form(nr=0)
br['memberId'] = username
br['passWord'] = password
response = br.submit()
print response.geturl()
print response.read()
'''
print "Send username and password"
print "Redirect..."
print response.geturl()

br.select_form(nr=0)
br['simpleSearch']='3382'
response = br.submit()
print "Using simple search"
print response.geturl()
print response.read()
'''
'''
html = br.response().read()
bs = BeautifulSoup(html,'lxml')
for links in bs.findAll('a'):
  if "href" and "pdf" in links.get("href"):
    for link in links:
       print link
'''
'''
  for link in links:
    print link
    download_urls = []
    href = link.get('href')
    print href
'''
'''
    if "href" and "pdf" in href:
      download_urls.append(href)
  for download_url in download_urls[:5]:
    time.sleep(10)
    file_name = download_url.split("/")[-1]
    if url in download_url:
      r = requests.get(download_url)
    else:
      r = requests.get(url + download_url)

        # Save File
    if r.status_code == 200:
      f = open(file_name, 'w')
      f.write(r.content)
      f.close()
'''
'''
BASE_URL = u"https://researchdirect.smbcnikko.co.jp"
EXTENSION = u"pdf"

urls = [
    u"https://researchdirect.smbcnikko.co.jp",
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
         time.sleep(10)

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
'''
"""
directory = "/home/gci/GCI"
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
"""




"""
br.addheaders = [('User-agent', 'Mozila/5.0(X11; U; Linux i686; en-us; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
urllogin = "https://researchdirect.smbcnikko.co.jp/"
username = "shinichiro.ueno@gci.jp"
password = "gcigci"
br.open(urllogin)
print('シボレス認証にアクセスしました')
br.select_form(nr = 0)
br['j_username'] = username
br['j_password'] = password
br.submit()
print('ユーザ名及びパスワードを入力、送信しました。')
print('リダイレクト中です。')
br.select_form(nr = 0)
br.submit()
print('学務課公式サイトにアクセスしました。')
html = br.response().read()
bs = BeautifulSoup(html, 'lxml')
print('通知を検索中です。')
print('-'*20)
for t in bs.findAll('p', {'class':'info_message'}):
    print(t.text.strip())
else:
    print('-'*20)
    print('現在上記の通知が出ています。')
"""

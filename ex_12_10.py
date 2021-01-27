# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = input("Enter Position: ")
count= input("inter Count: " )
c=int(count)
p=int(position)
print('Retriving:', url)
for i in range(c):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        url=tags[p-1].get("href", None)
    print('Retriving:',url)
    # print(tag.get('href', None))
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ("Enter url:")
xml = urllib.request.urlopen(url, context=ctx)
data = xml.read()
stuff = ET.fromstring(data)
lst= stuff.findall(".//count")
total = 0
for item in lst:
    total =total+ int(item.text)
print ("Retriving: ", url)
print ("Retrived: ", len(url), "charecters")
print("Count:", len(lst))
print("Sum:", total)
# total = stuff.find(("count").text)
# print(total)

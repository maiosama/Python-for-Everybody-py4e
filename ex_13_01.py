import urllib.request, urllib.parse, urllib.error
import ssl
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Location: ")
print("Retreiving", url)
uh=urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved" , len(data), "characters")

info= json.loads(data)
count=0
sum=0
for item in info['comments']:
        count+=1
        sum=sum+(item['count'])
print("count: ",count)
print("sum: ", sum)

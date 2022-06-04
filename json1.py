import json
import ssl
import urllib.request, urllib.parse, urllib.error

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_1379543.json'

url_read = urllib.request.urlopen(url, context=ctx).read()
url_json = json.loads(url_read)
coms = url_json.get('comments', None)

total = []

for obj in coms:
    total.append(int(obj.get('count', None)))
    
print(sum(total))
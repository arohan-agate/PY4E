import json
import ssl
import urllib.request,urllib.parse, urllib.error



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"

data_address = "University of West Florida"
address_wanted = data_address


parameters = {"address": address_wanted, "key":api_key}
paramsurl = urllib.parse.urlencode(parameters)


queryurl = serviceurl.strip() + paramsurl.strip()
print("DATA URL: ", queryurl)

data_read = urllib.request.urlopen(queryurl , context=ctx).read()
data = data_read.decode()

jsondata = json.loads(data)
print(jsondata)
place_id = jsondata["results"][0]["place_id"]
print("PLACE ID: ", place_id)
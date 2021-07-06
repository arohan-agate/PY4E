import urllib.request,urllib.parse,urllib.error
import json

url = input("Enter URL: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1290771.json"
print("Retrieving", url)

connection = urllib.request.urlopen(url)
data = connection.read().decode()
print("Retrieved:", len(data), "characters")

js = json.loads(data)

print('Count:', len(js["comments"]))

total = 0
for item in js["comments"]:
    num = int(item["count"])
    total += num
print("Sum:", total)

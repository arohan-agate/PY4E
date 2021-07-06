import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

url = input("Enter URL: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_1290770.xml"
print("Retrieving", url)

xml = urllib.request.urlopen(url).read()  # reads the URL, assigns it to the XML variable
print("Retrieved:", len(xml), "characters")

tree = ET.fromstring(xml)  # tree is a tree of information
counts = tree.findall('.//count')  # searches for all the "user" tags below "users". get both tags (as trees) in a list
print("Count:", len(counts))  # prints the length of the array of counts

total = 0;
for count in counts:  # loops through every element in the list of count values
    total += int(count.text)  # finds the sum of all the count values in the XML

print("Sum:", total)
# Web Scraping
# When a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts
# information, and then looks at more web pages. Search engines scrape web pages.
import urllib.request, urllib.parse, urllib.error  # importing the urllib library
from bs4 import BeautifulSoup  # importing the BeautifulSoup library

url = input('Enter - ')  # ask for a URL
html = urllib.request.urlopen(url).read()  # open the url and do a .read() (reads everything with newlines at the end
# of each line. reads it all as 1 string.
soup = BeautifulSoup(html, 'html.parser')  # BeatifulSoup parses the whole file. the soup object holds a cleaned up
# version of all the HTML tags and text

# Retrieve all of the anchor tags (aka HyperText)
tags = soup('a')  # creates a list of all the anchor tags in the document
for tag in tags:  # iterates through each of the anchor tags in the list
    print(tag.get('href', None))  # gets the URLs of each anchor tag
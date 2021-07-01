# Using urllib in Python.
# Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file.
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')  # pass in a URL as a parameter. returns a file handle.
# urlopen gets rid of the headers and only shows the data.
for line in fhand:  # this loop will iterate through all lines of the handle (data from the URL)
    print(line.decode().strip())  # must decode each line so that it is displayed as a string.

# Like a File...
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
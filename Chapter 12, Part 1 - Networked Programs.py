# Sockets in Python
# Sockets are a way for a client and a server to trade information back and forth.

# HTTP (HyperText Transfer Protocol)
# The set of rules to allow browsers to retrieve web documents from servers over the Internet

# URLs http:// -> protocol www.dr-chuck.com -> host /page1.htm -> document.
# When a user clicks on a URL to switch to a new page, the browser makes a socket connection to the web page and a "GET"
# request is issued. The server returns the HTML document to the browser, which is displayed to the user.

# An HTTP Request in Python (Make a connection to a port, send a 'GET' request, get some data back)
import socket  # you must import the socket library

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # returns an object to the mysock variable
mysock.connect(('data.pr4e.org', 80))  # makes the connection. like dialling the phone. the URL is the host. the
# number is the port\
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)  # the initialized socket is sending the 'GET' request detailed in like 17.

while True:
    data = mysock.recv(512)  # .recv() is a method in the socket object. Receives up to 512 characters
    if (len(data) < 1):  # if you get no data... you break out of the loop
        break
    print(data.decode())  # if you got data, you decode it. It prints the metadata and the text
mysock.close()  # closes the connection between your program and the web page


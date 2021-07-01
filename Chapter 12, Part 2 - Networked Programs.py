# ASCII (American Standard Code for Information Interchange)
# In ASCII, each character had a number associated with it. Only 128 characters.
# The ord() function tells us the numeric value for a simple ASCII character
ord('H')  # 72
ord('e')  # 101
ord('\n')  # 10

# Unicode
# A universal code for hundreds of character sets. UTF-8 is the most common way of representing
# characters. UTF is compatible with ASCII. UTF is the best for moving files or network data between two systems.

# Two Kinds of Strings in Python
# In Python 3, regular strings and unicode strings are both considered to be of type string.
# Byte strings are of a different type than regular or unicode strings.

# Python Strings to Bytes
# When we read data from an external source, it must be decoded based on the character set so that it is properly
# displayed as a string.
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    mystring = data.decode()  # you can pass in a character set as a parameter, but it defaults to UTF-8 or ASCII
    print(mystring)

# An HTTP Request in Python
# .encode() takes a string and turns it into bytes. The bytes are then sent to the server out the command.

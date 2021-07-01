#Using open()
#handle = open(filename, mode) -> fhand = open("mbox.txt", "r")
#filename is a string. mode is optional, "r" to read the file, "w" to write the file.
#--------------------------------------------------------------------------------------#
#Newline Character
phrase = "X\nY"
print(phrase)
#Newline is treated as 1 character
print(len(phrase))
#--------------------------------------------------------------------------------------#
#File Processing
# A text file has newlines at the end of each line
#--------------------------------------------------------------------------------------#
#File Handle as a Sequence
# each line in the file is a string in the sequence
xfile = open("test.txt")
for cheese in xfile:
    print(cheese)
#--------------------------------------------------------------------------------------#
#Counting Lines in a File
xfile = open("test.txt")
count = 0
for line in xfile:
    count += 1
#--------------------------------------------------------------------------------------#
#Reading the Whole File
xfile = open("test.txt")
inp = xfile.read() #reads everything on the same line -> ......\n........-> Printing it out will show the new lines.
#--------------------------------------------------------------------------------------#
#Searching Through a File
xfile = open("test.txt")
for line in xfile:
    line = line.rstrip() #strips off the newline at the end of each line. print() already adds a newline
    if line.startswith("From:"):
        #print(line)
# --------------------------------------------------------------------------------------#
#Skipping with Continue
xfile = open("test.txt")
for line in xfile:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue #skips all lines that don't start with "From:"
    #print(line)
#--------------------------------------------------------------------------------------#
#Using in to Select lines
xfile = open("test.txt")
for line in xfile:
    line = line.rstrip()
    if not "@utc.ac.za" in line:
        continue #skips the lines that do not contain "@utc.ac.za"
    #print(line)
#--------------------------------------------------------------------------------------#

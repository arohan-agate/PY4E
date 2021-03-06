#strings have indexes
fruit = "banana"
letter3 = fruit[2]

#the len function returns the length of a string
string_length = len(fruit)

#looping through strings
fruit = "banana"
for x in fruit:
    print(x)

#looping and counting
word = "supercalifragilisticexpialidocious"
count = 0
for letter in word:
    if letter == "a":
        count+=1

#slicing strings
s = "Monty Python"
print(s[0:4])
print(s[6:100])
print(s[:2]) #print all letters before 2nd index
print(s[8:]) #print all letters after and including 8th index
#using "in" as a Logical Operator
word2 = "hello"
var = "e" in str  #evaluates to True

#string comparision
if word < "banana":
    #word comes before "banana"
elif word > "banana":
    #word comes after "banana"
if "Z" < "a":
    #statement will execute

#String Library
"Hello Bob".lower() -> "hello bob"
"ABC".capitalize() -> "Abc"
"abc".capitalize() -> "Abc"

#Searching a String
fruit = "banana"
pos = fruit.find("na") #pos holds a value of 2
pos = fruit.find("z") #pos holds a value of -1.

#Search and Replace
greet = "Hello Bob"
nGreet = greet.replace("Bob", "Jane") #holds the string value of "Hello Jane". REPLACES ALL OCCURRENCES

#Stripping Whitespace
#.lstrip() and .rstrip() remove whitespace at the left or right
#.strip() removes both beginning and ending whitespace

#Prefixes
line = "Please have a nice day"
line.startswith("Please") #returns True
line.startswith("p") #returns False

#Parsing and Extracting
data = "From stephen.marquard@utc.ac.za Sat Jun 5 09:14:16 2008"
atpos = data.find("@") #atpos holds a value of 21, the location of the @ in the string
sppos = data.find(" ", atpos) #finds the index of the FIRST space AFTER the second parameter, ATPOS... sppos holds a value of 31
host = data[atpos+1 : sppos] #slices the string from 1 after the @ to the first space. HOLDS A VALUE OF "utc.ac.za"
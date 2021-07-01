# Tuples
x = ('Glenn', 'Sally', 'Joseph')
x[2]  # returns the value 'Joseph'
y = (1, 9, 2)
max(y)  # returns a value of 9
for i in y:
    print(i)

# Tuples and Assignment
(x, y) = (4, 'fred')

# Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)
tups = d.items()
print(tups)

# Tuples are Comparable
var1 = (0, 1, 2) < (5, 1, 2)  # True
var2 = (0, 1, 200000) < (0, 3, 4)  # True
var3 = ('Jones', 'Sally') < ('Jones', 'Sam')  # True
var4 = ('Jones', 'Sally') > ('Adams', 'Sam')  # True

# Sorting Lists of Tuples
d = {'a': 10, 'b': 1, 'c': 22}
d.items()  # dict_items([('a', 10), ('c', 22), ('b', 1)])
sorted(d.items())  # [('a', 10), ('b', 1), ('c', 22)]

# Using sorted()
d = {'a': 10, 'b': 1, 'c': 22}
t = sorted(d.items())
for k, v in sorted(d.items()):  # sorted by key order, not value order
    print(k, v)
# a 10
# b 1
# c 22

# Sort by Values Instead of Key
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))  # puts the value first
tmp = sorted(tmp, reverse=True)  # sorts in descending order

# Finding the 10 most common words in a text file
fhand = open('romeo.txt')  # opens txt file
counts = dict()  # creates a dictionary
for line in fhand:  # loops through each line in the file
    words = line.split()  # adds all the words in each line to a list called words
    for word in words:  # loops through each element in the list words
        counts[word] = counts.get(word, 0) + 1  # creates the histogram of words and how often they appear in the
        # dictionary

lst = list()  # initializes an empty list
for key, val in counts.items():  # loops through key, value in the histogram dictionary
    newtup = (val, key)  # creates a new tuple, with value first, then key.
    lst.append(newtup)  # adds the new tuple to a list

lst = sorted(lst, reverse=True)  # sorts the list by value, in descending order

for val, key in lst[:10]:  # loops through the elements of index 0 through 10, not inclusive (first 10 values)
    print(key, val)  # prints out these values

#Dictonaries
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
purse['candy'] += 2 #adds 2 to the candy value in purse

#Dictonary Literals
jjj = {'age' : 16, 'temp' : 92, 'grade' : 4}
eee = {}

#Many Counters with a Dictionary
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

#The get Method for Dictionaries
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0)

#Simplified Counting with get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1 #sets the count of the name to be the current count or 0, and then add 1 to it
print(counts)

#Application of counting with Dictionaries
counts = dict()
line = input('Enter a line of text: ')
words = line.split()
for word in words:
    counts[word] = counts.get(word, 0) + 1

#Definite Loops and Dictionaries
counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts:
    print(key, counts[key])

#Retrieving lists of Keys and Values
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
list(jjj) #returns a list of the keys in the dictonary
jjj.keys() #returns list of keys
jjj.values() #returns a list of values

#Two Iteration Variables
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key, value in jjj.items(): #FIRST variable is KEY, SECOND variable is VALUE
    print(key, value)
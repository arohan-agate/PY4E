#A List is a kind of Collection
fruits = ["apples", "bananas", "oranges"]
random = ["red", 24, 98.6, [5, 6]]
empty = []
#Lists and Definite Loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print(friend, "is my friend.")
#Looking Inside Lists
friends = ['Joseph', 'Glenn', 'Sally']
best_friend = friends[1] #holds a value of 'Glenn'
#Lists are Mutable
nums = [1, 2, 3, 4]
nums[2] = 10 #assigns the 2nd index (3rd spot) in the list to be 10
#List Length
x =[1, 2, ['Bob', 'Joe'], 93.4]
len(x) #length of x is 4
len(x[2]) #length of 3rd element, equal to 2
#Using the Range Function
#returns a list of numbers from 0 to 1 less than the parameter
range(4) #returns a list of [0, 1, 2, 3]

friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)

#Concatenating Lists
a = [1, 2, 3]
a += [4, 5, 6]
b = [4, 5, 6]
a += b
c = a + b

#Slicing Lists
t = [9, 41, 12, 3, 74, 15]
t[1:3] #returns [41, 12]
t[:4] #[9, 41, 12, 3]

#Building a List from Scratch
stuff = list()
stuff.append('book')
stuff.append(99)

#Is Something in a List?
some = [1, 9, 21, 10, 16]
9 in some #True
15 in some #False

#Lists are in Order
int_sample = [4, 1, 3, 9, 8, 5, 8, 6, 7]
int_sample.sort() #sorts the list in ascending order
str_sample = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
str_sample.sort() #sorts alphabetically
sorted(str_sample)

#Built-in Functions and Lists
nums = [1, 2, 3, 4]
max(nums)
min(nums)
sum(nums)

#Strings and Lists
abc = 'With three words'
stuff = abc.split()
thing = 'first;second;third'.split(';')
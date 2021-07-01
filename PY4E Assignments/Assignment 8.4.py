fname = input('Enter file name: ')
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    temp_list = line.split()
    for word in temp_list:
        if word not in lst:
            lst.append(word)
print(sorted(lst))
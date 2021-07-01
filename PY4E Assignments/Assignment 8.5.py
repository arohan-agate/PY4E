fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
	line = line.rstrip()
	if line.startswith("From "):
		count += 1
		words = line.split()
		print(words[1])
print("There were", count, "lines in the file with From as the first word")
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
hours = []

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        hour = words[5].split(':')
        counts[hour[0]] = counts.get(hour[0], 0) + 1

for key, val in counts.items():
    hours.append((key, val))

lst = sorted(hours)
for key, val in lst:
    print(key, val)
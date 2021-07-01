name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

most_sent = dict()

for line in handle:
    line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    most_sent[words[1]] = most_sent.get(words[1], 0) + 1

largest = None
high_sender = None

for key in most_sent:
    if largest is None:
        largest = most_sent[key]

    if largest < most_sent[key]:
        largest = most_sent[key]
        high_sender = key

print(high_sender, largest)
fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print("Invalid file name:", fname)
    quit()

tC = 0
count = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    line = line[19:]
    tC += float(line)

print("Average spam confidence:", (tC/count))

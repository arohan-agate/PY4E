import re

file = open('Actual-Data.txt', 'r')

total = 0

for line in file:
    nums = re.findall('[0-9]+', line)
    for num in nums:
        total += int(num)

print(total)
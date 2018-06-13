from collections import Counter

file_name = '../../py3intro/DATA/passwd'
counter = Counter()

try:
    file = open(file_name)
except IOError:
    print("ERROR: Could not open file", file_name)

for line in file:
    fields = line.split(":")
    shell = fields[-1][:-1]
    counter[shell] += 1

for shell, count in counter.items():
    print(shell, count)

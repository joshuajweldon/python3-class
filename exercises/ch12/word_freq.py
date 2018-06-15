import sys
import re
from collections import Counter

regex = "\W"
patter = re.compile(regex)

counter = Counter()

if len(sys.argv) != 2:
    print("USAGE: word_freq <filename>")
    exit(1)

filename = sys.argv[1]

try:
    file = open(filename)
    text = file.read()
except IOError:
    print("IO ERROR: with file ", filename)
    exit(2)

for item in patter.split(text):
    counter[item.lower()] += 1

for word, count in sorted(counter.items(),key=lambda x: x[1], reverse=True):
    if not word:
        continue
    print(word, count)

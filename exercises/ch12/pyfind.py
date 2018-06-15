import sys
import re

if len(sys.argv) < 3:
    print("USAGE: pyfind.py <regex> <filename> [<filename> ...]")
    exit(1)

regex = sys.argv[1]
filenames = sys.argv[2:]

try:
    pattern = re.compile(regex)
except Exception:
    print("ERROR: Regex is not recognized")
    exit(2)

for filename in filenames:
    print("Searching ", filename)
    try:
        file = open(filename)
        for line_num, line in enumerate(file, 1):
            if pattern.search(line):
                print(line_num)
        print()
        file.close()
    except IOError:
        print("IO ERROR: with file ", filename)
        print()
        continue


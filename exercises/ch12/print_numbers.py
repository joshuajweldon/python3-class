import re

regex = '^(\d{3}-)?\d{3}-\d{4}$'
pattern = re.compile(regex)

try:
    filename = '../../py3intro/DATA/custinfo.dat'
    file = open(filename)
except IOError:
    print("ERROR: could not open file", filename)
    exit()

for line in file:
    if pattern.search(line):
        print(line[:-1])

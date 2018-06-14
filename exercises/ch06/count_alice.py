file_name = '../../py3intro/DATA/alice.txt'
count = 0

try:
    file = open(file_name)
except IOError:
    print("ERROR: Could not open file", file_name)
    exit(1)

for line in file:
    if 'Alice' in line:
        count += 1

file.close()

print("'Alice' is seen on", count, "lines")

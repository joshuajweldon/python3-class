file_name = '../../py3intro/DATA/alt.txt'
a_file_name = 'a.txt'
b_file_name = 'b.txt'

try:
    file = open(file_name)
    a_file = open(a_file_name, "w")
    b_file = open(b_file_name, "w")
except IOError:
    print("ERROR: Could not open file(s)")
    exit(1)

for line in file:
    if line[0] == 'a':
        a_file.write(line)
    elif line[0] == 'b':
        b_file.write(line)
    else:
        print("ERROR: line does not begin with an 'a' or 'b' -", line)

file.close()
a_file.close()
b_file.close()

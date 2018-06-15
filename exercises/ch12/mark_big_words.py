import re

regex = "\w{8,}"
pattern = re.compile(regex)

try:
    parrot_file = open('../../py3intro/DATA/parrot.txt')
    bigwords_file = open('bigwords.txt', 'w')
    text = parrot_file.read()
except IOError:
    print("ERROR: Could not open files")
    exit(1)

offset = 0
for item in pattern.finditer(text):
    start = item.start() + offset
    end = item.end() + offset
    text = text[:start] + '*' + text[start:end] + '*' + text[end:]
    offset += 2

bigwords_file.write(text)
parrot_file.close()
bigwords_file.close()
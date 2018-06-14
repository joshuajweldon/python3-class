import sys


def count_words(word, file_name):
    count = 0

    try:
        file = open(file_name)
    except IOError:
        print("ERROR: Could not open file", file_name)
        exit(1)

    for line in file:
        if word.upper() in line.upper():
            count += 1

    file.close()

    return count


if len(sys.argv) < 2:
    print("USAGE: count_words.py <word> <file path> [<file path> ...]")
    exit(1)

my_word = sys.argv[1]
file_names = sys.argv[2:]

for curr_file_name in file_names:
    curr_count = count_words(my_word, curr_file_name)
    print(curr_file_name, curr_count)

import sys


def print_file(file_name):
    try:
        file = open(file_name)
    except IOError:
        print("ERROR: Could not open file", file_name)
        return

    for index, line in enumerate(file, 1):
        print(index, line, end="")

    file.close()


if len(sys.argv) < 1:
    print("USAGE: line_no.py <file path> [<file path> ...] ")
    exit(1)

file_names = sys.argv[1:]

for curr_file_name in file_names:
    print_file(curr_file_name)
    print()

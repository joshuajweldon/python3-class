while True:
    filename = input("filename: ").strip()

    try:
        file = open(filename)
    except IOError:
        print("ERROR: could not open file,", filename)
    else:
        break

for line in file:
    line = line[:-1]
    try:
        x, y = line.split()
        x = float(x)
        y = float(y)
        r = x / y
    except (ValueError, ZeroDivisionError):
        print("ERROR: could not compute line,", line)
    else:
        print(r)

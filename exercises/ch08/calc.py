def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x*y


def divide(x, y):
    try:
        r = x / y
    except ZeroDivisionError:
        r = "Undef."
    return r


operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

input("Calculator Application: \nYou may enter an expression of the form x [+-*/]+ y.\nYou my enter 'q' to quit. \nPress ENTER to start.")

while True:
    expression = input(">>> ")

    if not expression:
        continue

    if expression == 'q':
        break

    try:
        curr_x, op, curr_y = expression.split()
    except ValueError:
        print("Error: expression must be of the form x [+-*/]+ y")
        continue

    try:
        curr_x = float(curr_x)
        curr_y = float(curr_y)
    except ValueError:
        print("Error: both x ({})and y ({}) must be real numbers".format(curr_x, curr_y))
        continue

    print(operators.get(op, "Invalid Operator ({})".format(op))(curr_x, curr_y))

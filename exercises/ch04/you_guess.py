import sys
import random

val = random.randint(1, 100)
count = 0
high = 100
low = 1

print("Game Rules: I'm thinking of a number from {} to {}".format(low, high))
print("            Try to guess the number in the least amount of tries")
print("            When you are ready press ENTER to play")

input()

while True:

    count += 1

    guess = input("What number am I thinking of: ")

    try:
        guess = int(guess)
    except ValueError:
        print("That is not a valid number.")
        continue

    if guess > val:
        print('Too High')
    elif guess < val:
        print('Too Low')
    elif guess == val:
        print('You Won in {} tries!'.format(count))
        break

import sys

high = 100
low = 1

print("Game Rules: Pick a number from {} to {}".format(low, high))
print("            If the computer's guess is too HIGH press 'h'")
print("            If the computer's guess is too LOW press 'l'")
print("            If the computer's guess is correct press 'y'")
print("            When you are ready press ENTER to play")

input()

while True:
    if low > high:
        print('You lie! GAME OVER')
        break

    mid = (high + low) // 2
    user_input = input("Is your number {}: ".format(mid))

    if user_input == 'y':
        print('GAME OVER')
        break
    elif user_input == 'l':
        low = mid + 1
    elif user_input == 'h':
        high = mid - 1
    else:
        print("Error: Invalid Input")
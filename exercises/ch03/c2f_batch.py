import sys

temperature = 0

if len(sys.argv) == 2:
    temperature = sys.argv[1]
else:
    print("Error: Must have the temperature as an argument.")
    exit(1)

try:
    temperature = float(temperature)
except ValueError:
    print("Error: incorrect number format")
    exit(1)

#convert to fahrenheit
temperature = ((9*temperature) / 5) + 32

print(temperature)
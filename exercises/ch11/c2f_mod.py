from temp_conv import *

temperature = input("Enter temperature in celsius: ")

try:
    temperature = float(temperature)
except ValueError:
    print("Error: incorrect number format")
    exit(1)

# convert to fahrenheit
temperature = c2f(temperature)

print("Fahrenheit = ", temperature, "\u00b0F")

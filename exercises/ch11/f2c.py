from temp_conv import *

temperature = input("Enter temperature in fahrenheit: ")

try:
    temperature = float(temperature)
except ValueError:
    print("Error: incorrect number format")
    exit(1)

# convert to fahrenheit
temperature = f2c(temperature)

print("Celsius = ", temperature, "\u00b0F")

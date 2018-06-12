import sys

temperature = input("Enter temperature in celcius: ")

try:
    temperature = float(temperature)
except ValueError:
    print("Error: incorrect number format")
    exit(1)

#convert to fahrenheit
temperature = ((9*temperature) / 5) + 32

print("Fahrenheit = ", temperature, "\u00b0F")


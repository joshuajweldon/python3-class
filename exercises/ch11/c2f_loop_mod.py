from temp_conv import *

while True:
    temperature = input("Enter temperature in celsius: ")

    if temperature == 'q':
        break

    try:
        temperature = float(temperature)
    except ValueError:
        print("Error: incorrect number format")
        continue

    # convert to fahrenheit
    new_temperature = c2f(temperature)

    print(temperature, "\u00b0C -> ", new_temperature, "\u00b0F")

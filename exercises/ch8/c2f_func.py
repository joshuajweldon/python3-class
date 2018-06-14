def c2f(ctemp):
    '''takes in a temperature in celcius and return it in fahrenheit'''
    return ((9*ctemp) / 5) + 32

test_temps = (100, 0, 37, -40)

for temp in test_temps:
    print(temp, "\u00b0C ->", c2f(temp), "\u00b0F")


fruits = ['      Apple    ', '      Pear      ', '        Banana       ', '          Grapes         ']

clean_fruits = (fruit.lower().strip() for fruit in fruits)

print(" ".join(clean_fruits))

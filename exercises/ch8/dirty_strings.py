def cleanup(dirty_string: str):
    '''trims white space and sets word to lower case'''
    return dirty_string.strip().lower()

spam = [
    "Spam",
    "eggs  ",
    "   spam    ",
    "     spam spam     ",
    "SPAM	",
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

for word in spam:
    print(cleanup(word))


import re

def palindrome(string):
    string = str(string) # must be converted to str to test with numbers

    clean_string = re.sub(r'[^a-zA-Z0-9]', '', string).lower() # get rid of whitespace, punctuation

    return clean_string == clean_string[::-1]

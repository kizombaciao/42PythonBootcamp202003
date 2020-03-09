import string
import re   # regular expression library

def text_analyzer(lst = None):
    """Counts the number of upper, lower, punctuation, spaces"""

    if lst is None:
        lst = input('What is the text to analyze?\n')
    upp = len(re.findall(r'[A-Z]', lst))
    low = len(re.findall(r'[a-z]', lst))
    pun = sum(lst.count(c) for c in string.punctuation)
    spa = len(re.findall(r' ', lst))

    print('The text contains 143 characters: ')
    print('- {} upper letters'.format(upp))
    print('- {} lower letters'.format(low))
    print('- {} punctuation marks'.format(pun))
    print('- {} spaces'.format(spa))

# findall = returns a list containing all matches
# print(string.punctuation)
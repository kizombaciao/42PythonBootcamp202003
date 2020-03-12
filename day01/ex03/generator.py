import random

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''

    choices = ['shuffle', 'unique', 'ordered']

    ttt = text.split(sep)
    if option == 'shuffle':
        ttt2 = random.shuffle(ttt)
    elif option == 'unique':
        ttt2 = set(ttt)
    else:
        ttt2 = ttt.sort()

    for i in ttt:
        yield(i)

#    print(ttt)


yy = generator('what is this', option='sort')
print(next(yy))
print(next(yy))
print(next(yy))


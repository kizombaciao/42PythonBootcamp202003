b1 = 'abc'
b2 = 'def'
b3 = 'xyz'

def blog(*args):
    print(type(args))
    print(args)

blog(b1, b2, b3)

def kblog(**kwargs):
    print(type(kwargs))
    for a, b in kwargs.items():
        print(a, b)

kblog(bb1='a', bb2='b', bb3='c')
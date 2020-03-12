def what_are_the_vars(*args, **kwargs):
    for i in args:
        setattr()

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print('Error')
        print('end')
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print('{}: {}'.format(attr, value))
    print('end')

if __name__ == '__main__':
    obj = what_are_the_vars(7)

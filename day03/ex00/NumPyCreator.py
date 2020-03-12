import array as arr

# print(type(range(5)))

def rr(*args):
    print(arr(args))

class NumPyCreator(object):
    def __init__(self, *args):
        self.lst = args
        print(type(args))

    def ppp(self):
        print(self.lst)
        print(type(self.lst))


t = [[1,2],[3,4]]
t1 = NumPyCreator([5,6],[7,8])
t1.ppp()

rr([1,2])

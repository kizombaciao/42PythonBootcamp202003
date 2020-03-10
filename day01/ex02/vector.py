import math

class Vector(object):
    def __init__(self, *args):
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args
        self.size = len(args)
        #print(self.values)
        print(self.size)

#    def __add__(self, other):
#        return(Vector(self.values[i] + other.values[i]))




tt = Vector([1,2,3])
print(tt.values)

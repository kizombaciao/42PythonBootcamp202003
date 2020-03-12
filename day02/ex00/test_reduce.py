from functools import reduce

data = range(1, 5)
print(data)

mult = lambda x, y: x * y
t1 = reduce(mult, data)
print(t1)


import sys

s = ' '.join(sys.argv[1:])
#print(s)
s = s[::-1]
#print(s)
s = s.swapcase()
print(s)

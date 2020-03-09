import sys
import string

av = sys.argv[1:]

if len(av) != 2 or av[0].isdigit()== True or av[1].isdigit() == False:
    print('ERROR')
    exit(1)

s = av[0]
l = int(av[1])
tmp = [c for c in s if c not in set(string.punctuation)]
s = (''.join(tmp)).split()
lst = [e for e in s if len(e) > l]
print(lst)

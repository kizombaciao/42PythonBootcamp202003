file = open('file.txt', 'w')
try:
    file.write('hello\n')
finally:
    file.close()

with open('file.txt', 'a') as f:
    f.write('hello2')

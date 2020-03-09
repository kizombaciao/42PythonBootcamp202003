import sys

if len(sys.argv) != 2:
    print('Error')
    exit(1)

try:
    whois = int(sys.argv[1])
    if (whois == 0):
        print('Zero')
    elif (whois%2 != 0):
        print('Odd')
    else:
        print('Even')
except ValueError:
    print('Error')
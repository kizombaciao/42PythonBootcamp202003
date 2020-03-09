import sys

def do_op(a, b):
    try:
        print('Sum:         {}'.format(a + b))
        print('Difference:  {}'.format(a - b))
        print('Product:     {}'.format(a * b))
        print('Divide:      {}'.format(a / b))
        print('Modulus:     {}'.format(a % b))
    except ZeroDivisionError:
        print('ERROR (DIVISION BY ZERO)')
        print('ERROR (MODULO BY ZERO)')

av = sys.argv[1:]

for i in av:
    if not i.isdigit():
        print('Usage: python operations.py <number1> <number2>')
        print('Example:')
        print('     python operations.py 10 3')
        print('InputError:  only numbers')
        sys.exit()

if len(av) != 2:
    print('Usage: python operations.py <number1> <number2>')
    print('Example:')
    print('     python operations.py 10 3')
    if len(av) > 2:
        print('InputError:  too many argumnts')
        sys.exit()
    print('InputError:  too few arguments')
    sys.exit()

a = int(av[0])    
b = int(av[1])    

do_op(a, b)

# prints the results of the four elementary mathematical operations of arithmetic (addition, subtraction, multiplication, division) and the modulo operation
# a function that takes 2 numbers as parameters and returns 5 values


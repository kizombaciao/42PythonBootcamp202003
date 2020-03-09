import sys

__infos = {
    'ingredients': [],
    'meal': 'lunch',
    'prep_time': 60,
    }

cookbook = {
    'sandwich': dict(__infos),
    'cake': dict(__infos),
    'salad': dict(__infos),
    }

def __add_recipe(name=None, ingredients=[], meal=None, prep_time=None):
    if name is None:
        print('Your recipe needs a name.')
        return
    elif not len(ingredients):
        print('Your recipe needs ingredients.')
        return
    elif meal is None:
        print('Your recipe needs a meal type.')
        return
    elif prep_time is None:
        print('Your recipe needs a preparation time.')
        return

def __print_menu():
    print("1. Add a recipe")
    print("2. Delete a recipe")
    print("3. Print a recipe")
    print("4. Print the cookbook")
    print("5. Quit")

def __sel_handler(sel):
    if sel < 1 or sel > 5:
        print('No such selection.')
    if sel == 1:
        sel2 = input('Enter a name: ')
        sel3 = input("Enter a list of ingredients (separated by spaces): ")
        sel4 = input("Enter a meal type: ")
        sel5 = input("Enter a preparation time: ")
        __add_recipe(sel2, sel3.split(' '), sel4, sel5)
    elif sel == 2:
        pass
    elif sel == 3:
        pass
    elif sel == 4:
        pass
    elif sel == 6:
        print('Cookbook closed.')
        sys.exit(0)
    

def menu():
    while True:
        __print_menu()
        sel = input("Please select an option by typing the corresponding number:")
        if not sel.isdigit():
            print('Please input a number.')
        else:
            __sel_handler(int(sel))

menu()
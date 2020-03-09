import sys

cookbook = {
        'sandwich' : {
            'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
            'meal' : 'lunch',
            'prep_time' : '10'
        },
        'cake' : {
            'ingredients' : ['flour', 'sugar', 'eggs'],
            'meal' : 'dessert',
            'prep_time' : '60'
        },
        'salad' : {
            'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
            'meal' : 'lunch',
            'prep_time' : '15'
        }
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
    cookbook.update({name:{'ingredients':ingredients, 'meal':meal, 'prep_time':prep_time}})

def __del_recipe(name=None):
    if name is None:
        print('Need to pick a recipe.')
        return
    elif name not in cookbook:
        print('Recipe not found.')
        return
    else:
        del cookbook[name]
        print('Recipe {} deleted.'.format(name))

def __print_recipe(name=None):
    if name is None:
        print('Need to pick a recipe.')
    elif name not in cookbook:
        print('Recipe not found.')
    else:
        print('Recipe for {}:'.format(name))
        print('Ingredients list: {}'.format(cookbook[name]['ingredients']))
        print('To be eaten for {}.'.format(cookbook[name]['meal']))
        print('Preparation time is {} minutes.'.format(cookbook[name]['prep_time']))

def __print_recipe_all():
    for k, _ in cookbook.items():
        __print_recipe(k)

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
        sel2 = input('Please enter the recipe to delete:  ')
        __del_recipe(sel2)
    elif sel == 3:
        sel2 = input('Please enter a recipe to print: ')
        __print_recipe(sel2)
    elif sel == 4:
        __print_recipe_all()
    elif sel == 5:
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
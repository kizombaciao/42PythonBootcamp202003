import sys

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description='no description'):
        
        if not isinstance(name, str):
            raise TypeError('error: name has to be a string')
        if not isinstance(cooking_lvl, int):
            raise TypeError('error: cooking level has to be an unsigned integer')
        elif not 1 <= int(cooking_lvl) <= 5:
            raise ValueError('error: cooking level needs to be between 1 and 5')
        if not isinstance(cooking_time, int):
            raise TypeError('error: cooking time has to be an unsigned integer')
        elif not 0 < int(cooking_time):
            raise ValueError('error: cooking time needs to be above zero')
        if not ingredients:
            raise ValueError('error: ingredients can not be empty')
        elif not isinstance(ingredients, list):
            raise TypeError('error: ingredients have to be a list')
        if not isinstance(recipe_type, str):
            raise TypeError('error: recipe type has to be a string')
        elif recipe_type not in ['starter', 'lunch', 'dessert']:
            raise ValueError('error: recipe type must be starter, lunch or dessert')

        self.name = name
        self.cooking_lvl = int(cooking_lvl)
        self.cooking_time = int(cooking_time)
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        """return the string to print with recipe info"""
        txt = "Name: {}\nCooking level: {}\nCooking time: {}\nIngredients: {}\nRecipe type: {}\nDescription: {}".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.recipe_type, self.description)
        return txt


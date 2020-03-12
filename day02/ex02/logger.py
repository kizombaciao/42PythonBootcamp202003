import time
from random import randint

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print('Please add water!')
            return False
        
    @log
    def boil_water(self):
        return 'boiling...'

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
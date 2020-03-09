from random import randint

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.\nGood luck!")

count = 1
rnd = randint(1, 99)
n = int(input('What is your guess between 1 and 99?\n>> '))

while (n != rnd):
    if n > rnd:
        print('Too high!')
    elif n < rnd:
        print('Too low!')
    count += 1
    n = int(input('What is your guess between 1 and 99?\n>> '))
print(f'Congrats, total {count} guesses!')

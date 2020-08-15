# Guess My Number App
import random

print('\nWelcome to the guess number app.')

name = input('\n Enter your name : ').title().strip()

print('\n I\'ve choosen a number between 1 and 20. Can you guess the number ? ')
random_number = random.randint(1, 20)

for i in range(1, 6):
    guessed_number = int(input('\n Guess a number between 1 and 20 : '))

    if guessed_number > 20:
        print('\n Choose a number between 1 and 20 : ')
    elif guessed_number < random_number:
        print(f'\n It\'s higher than {guessed_number} ')
    elif guessed_number > random_number:
        print(f'\n It\'s lower than {guessed_number}')
    else:
        break
if guessed_number == random_number:
    print(f'\n Yay!{name}, You guessed it correct in {i}th time.')
else:
    print(f'\n Game over! The correct number was {random_number}')    
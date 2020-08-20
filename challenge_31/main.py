# The python Dice App
import random

def dice_sides() ->int:
    sides = int(input('\n Enter the sides of the dice. : '))
    return sides

def dice_number() -> int:
    number_of_dice = int(input('\n How many dices would you like to roll : '))
    return number_of_dice

def roll_dice(dice_sides:int,dice_count:int) -> list:
    dice_values = []
    print(f'\n Rolling {dice_count} dice with {dice_sides} sides each. ')
    for dice in range(dice_count):
        rolled_number = random.randint(1,dice_sides)
        dice_values.append(rolled_number)
    return dice_values    

def sum_dice(dice_values:list) -> None:
    total = sum(dice_values,0)
    print(f'\n Sum of all rolled dices {total}')

def roll_again() -> bool:
    response = input('\n Would you like to roll the dice again ? (y/n) ').lower()
    if response.startswith('y'):
        return True
    else:
        return False

#main program
if __name__ == "__main__":
    print('\n Welcome to the Dice Roll Game.')
    playing=True
    while playing:
        #prepare dice
        no_of_sides = dice_sides()
        no_of_dices = dice_number()

        rolled_values = roll_dice(no_of_sides,no_of_dices)
        sum_dice(rolled_values)
        playing = roll_again()
    print('\n Thank you for playing!')    

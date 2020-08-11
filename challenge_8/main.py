#Grocery List app
from datetime import datetime

grocery_list = set()

grocery_list.add('Meat')
grocery_list.add('Cheese')

date_time_now = datetime.now()
month : str = date_time_now.month
day : str = date_time_now.day
hour : str = date_time_now.hour
minute : str = date_time_now.minute

print('\n Welcome to the power store')
print(f'{month}/{day}::{hour}:{minute}')

print(f'\n Hey user, the list has {grocery_list} items')

for i in range(0,3):
    item = input('\n Enter an item : ')
    grocery_list.add(item.title())
    print(f'\n updated list : {grocery_list}')

sorted_list = sorted(grocery_list)
print(f'\n sorted grocery list : {sorted_list}')

print('\n simulating grocery list...')

for i in range(0,4):
    if len(grocery_list) == 2:
        new_food = input(f'Out of stock !! Enter something else :').title()    
        grocery_list.add(new_food)
        break   

    print(f'\n Current grocery list : {len(grocery_list)} items')
    print(f'\n {grocery_list}')
    last_purchased = input('What was your last purchase ? : ').title()
    print(f'\n Removing last purchased item : {last_purchased}')
    grocery_list.remove(last_purchased)

print(f'\n Your final grocery list : {grocery_list}')
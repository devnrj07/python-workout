#Factorial Calculator App
import math

print('\nWelcome to Factorial App')

number = int(input('Enter ther number you want factorial for : '))

print(f'{number}! = ',end="")
for i in range(1, number):
    print(f'{i}', end="*")
print(f'{number}')    

print(f'\n Factorial using library : {math.factorial(number)}')

def factorial(number : int):
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    return fact

result = factorial(number)
print(f'\n Factorial using own method : {result}')

#Summary
print("\nIt is shown twice that " + str(number) + "! = " + str(result) + " (with excitement!)")
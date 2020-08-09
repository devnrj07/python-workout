# Multiplication and Exponention Table

print('\nWelcome to Multiplication and Exponention Table app')

input_number= float(input(f'Hi, enter a number you want to generate a table for : '))

print(f'\n Multiplication table for {input_number} ')

for i in range(1,10):
    print(f'{input_number} * {float(i)} = {input_number * i}')

print(f'\n Exponent Table for {input_number} : ')

for i in range(1,10):
    print(f'{input_number} * {i} = {input_number ** i}')


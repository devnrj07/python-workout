#Factor Generator App

print('\n Welcome to the factor generator app.')
active = True

while active:
    user_input = int(input('\n Enter the number you want factors for : '))
    factors = list()
    for i in range(1,user_input+1):
        if user_input % i == 0:
            factors.append(i)
    print('\n Printing all the factors.') 
    print(f'\n All the factors for {user_input} are : {factors}')

    for i in range(int(len(factors)/2)):
        print(f'\n {factors[i]} * {factors[-i-1]} ')

    continue_program = input('\n Do you want to continue the program ? (y/n) : ').lower().strip()

    if continue_program.startswith('n'):
        active = False
        print('\n Have a nice day!')

#Even Odd sorted App

print('\n Welcome to the App')
active = True

while active :
    user_input = input('\n Enter a list of common seperated numbers : ').replace(' ','').split(',')
    evens = list()
    odds = list()

    for i in user_input:
        if int(i) % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    evens.sort()
    odds.sort()

    print(f'\n List of even numbers : {evens}')
    print(f'\n List of even numbers : {odds}')

    continue_program = input('\n Do you want to continue the program ? (y/n) : ').lower().strip()

    if continue_program.startswith('n'):
        active = False
        print('\n Have a nice day!')            
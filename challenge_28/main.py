# Prime Number App
import time

print('\n Welcome to the prime number app')

active=True

while active:
    program_type = input('\n What kind of prime no. app do you want (1/2/3) . : ')

    if program_type == '1':
        user_input_number = int(input('\n Enter the number you want to check :'))
        isPrime=True
        for i in range(2,user_input_number):
            if user_input_number%i == 0:
                isPrime=False
                break

        if isPrime:
            print(f'\n Entered number {user_input_number} is prime.')    
        else:
            print(f'\n Entered number {user_input_number} is not prime. ')    

    elif program_type == '2':
        lower_bound = int(input('\n Enter the lower bound for the range of numbers. '))
        upper_bound = int(input('\n Enter the upper bound for the range of numbers. '))        
        primes = list()
        start_time = time.time()
        for i in range(lower_bound, upper_bound+1):
            if i > 1:
                isPrime=True
                for j in range(2,i):
                    if i % j == 0:
                        isPrime=False
                        break
                                
            else:
                isPrime=False

            if isPrime:
                primes.append(i)
        end_time = time.time()
        delta_time = round(end_time - start_time, 4)
        print('\n Calculations took a total of'+ str(delta_time)+ ' seconds.')
        print("The following numbers between " + str(lower_bound) + " and " + str(upper_bound) + " are prime: ")
        input("Press enter to continue.")
        for prime in primes:
            print(prime)

    else:
        print('\n That is not a valid option.')

    continue_program = input('\n Do you want to continue the program ? (y/n) : ').lower().strip()
    if continue_program.startswith('n'):
            active = False
            print('\n Have a nice day!')     
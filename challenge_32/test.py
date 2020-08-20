# The calculator app

def add(a:float, b:float) -> float:
    print('\n performing addition operation ')
    return f'{a}+{b}={round(a+b,4)}'
def subtract(a:float, b:float) -> float:
    print('\n performing subtraction operation ')
    return f'{a}-{b}=round(a-b,4)'
def multiply(a:float, b:float) -> float:
    print('\n performing multiplication operation ')
    return f'{a}*{b} = {round(a*b,4)}'
def division(a:float, b:float) -> float:            
    print('\n performing division operation ')
    if b == 0:
        print('\n You cannot divide by zero.')
        raise Exception('Error: DIV ERROR')
    else:
        return f'{a}/{b} = {round(a/b,4)}'
def exponent(a:float, b:float) -> float:
    print('\n Performing exponential operation')
    return f'{a} ** {b} = {round(a**b,)}'

def continue_app() ->bool:
    response = input('\n Do you want to continue ? (y/n):').lower()
    if response.startswith('y'):
        return True
    else:
        return False    

if __name__ == "__main__":
    print('\n Welcome to the basic calculator app. ')
    active=True
    history = []
    while active:
        inputs = input('\n Enter the numbers comma separated : ').split(',')
        operation = input('\n Enter the type of operation you want to perform :').lower()
        arg_one = float(inputs[0])
        arg_two = float(inputs[1])
        if operation.startswith('a'):
            result = add(arg_one,arg_two)
            history.append(result)
            active = continue_app()
        elif operation.startswith('s'):
            result = subtract(arg_one,arg_two)
            history.append(result)
            active=continue_app()
        elif operation.startswith('m'):
            result = multiply(arg_one,arg_two)
            history.append(result)
            active=continue_app()        
        elif operation.startswith('d'):
            result = division(arg_one,arg_two)
            history.append(result)
            active=continue_app()
        elif operation.startswith('e'):
            result = exponent(arg_one,arg_two)
            history.append(result)
            active=continue_app()
        else:
            print('\n Invalid Operations. Operation not supported.') 
            history.append('Invalid Operation.')
            active=continue_app()
    print('Summary of your operations :')
    for operation in  history:
        print(f'\n {operation}')        
    print('\n Thank you for playing with us.')

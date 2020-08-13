# Quadratic Equation Solver App
import cmath

def solve_quadratic_equation(a:float,b:float,c:float):
    x1 = (-b + cmath.sqrt( b**2 - 4*a*c))/(2*a)
    x2 = (-b + cmath.sqrt( b**2 - 4*a*c))/(2*a)
    return x1,x2


print('\n Welcome to Quadratic Equation Solver. ')

number_of_equations = int(input('\n How many quadratic equations would you like to solve, ask for the coefficients of the equation in the standard form of ax 2 + b x + c = 0 , : '))

for i in range(number_of_equations):
    print(f'Solving Equation #{i+1}')
    print('---------------------------------')
    a = float(input('Enter the value of a (coefficient of X^2) : '))
    b = float(input('Enter the value of b (coefficient of X) : '))
    c = float(input('Enter the value of c (coefficient) : '))
    x1, x2 = solve_quadratic_equation(a,b,c)
    print(f"\nThe solutions to {a}x^2+{b}x+{c} = 0 are: ")
    print("\n\tx1 = " + str(x1))
    print("\tx2 = " + str(x2))

print("\nThank you for using the Quadratic Equation Solver App.Goodbye.")


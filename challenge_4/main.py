# find hypotenuse and area of a triangle 
from math import sqrt
print('\n Welcome to traingle rule APP ')

side_a = float(input('\n Enter the length of side one of the triangle. '))
side_b = float(input('\n Enter the length of side two of the triangle. '))

hypotenuse = round(sqrt(side_a**2 + side_b**2),2)
area = round(0.5 * side_a * side_b,2)

print(f'\n For a triangle with sides {side_a}, {side_b} the longest side is {hypotenuse}. ')
print(f'\nArea for the triangle is {area}')
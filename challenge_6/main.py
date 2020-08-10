#Grade sorted App

print('\nWelcome to the Grade Sorted App')

#initialize first or use append()/insert(x,ith)
grades = [None] * 4


for i in range(0,4):
  grades[i] = int(input(f'\n what is your grade in subject {i+1} : '))

print(f'\n You entered the following grades: {grades}')

#sort grades
grades.sort(reverse=True)
print(f'\n Highest to lowest grades: {grades}')

#remove last two grades

pop_elment = grades.pop(-1)
print(f'\n removing the grade {pop_elment}')
pop_elment = grades.pop(-1)
print(f'\n removing the grade {pop_elment}')

print(f'\n Updated grades : {grades}')
print(f'\n Highest grade: {grades[0]}')

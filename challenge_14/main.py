#Fibonacci Calculator app

print('\n Welcome to the fibonacci app.')

number = int(input('\n Enter the number of digits you want to compute fibonacci : '))

fibo_list = [1,1]

for i in range (number-2):
    new_fibo = fibo_list[i] + fibo_list[i+1]
    fibo_list.append(new_fibo)

print(f'\n The fibonacci sequence for {number} : ')
for i in fibo_list:
    print(f'\n{i}')

# golden ratio
golden_list = list(fibo_list)

for i in range(len(fibo_list)-1):
    gr = fibo_list[i+1]/fibo_list[i]
    golden_list.append(gr)

print(f'\n The corresponding golden ratio sequence for {number} : ')
for i in golden_list:
    print(f'\n{i}')





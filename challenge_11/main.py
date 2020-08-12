#Binary Hexadecimal Converter App

print('Welcome to the Binary to Hexadecimal Converter App')
number_of_items = int(input('Enter ther number of inputs you want to convert : '))

numbers_list = [i for i in range(1,number_of_items+1)]
print(f'list of numbers : {numbers_list}')
max_value = max(numbers_list)

binary_list = list()
hexadecimal_list = list()

for i in numbers_list:
    bin_number = bin(i)
    binary_list.append(bin_number)
    hex_number = hex(i)
    hexadecimal_list.append(hex_number)

print('The conversion is complete!')
start_number = int(input('where to start from ? : '))
end_number = int(input('Where to stop at ? :'))

start_index = numbers_list.index(start_number)
end_index = numbers_list.index(end_number)

display_binary_list = binary_list[start_index:end_index+1]
display_hexadecimal_list = hexadecimal_list[start_index:end_index+1]

print(f'List of binary : {display_binary_list}')
print(f'List of Hexadecimal : {display_hexadecimal_list}')

#Output the whole list to the screen
input("\nPress Enter to see all values from 1 to " + str(max_value) + ".")
print("Decimal----Binary----Hexadecimal")
print("----------------------------------------------")
for d, b, h in zip(numbers_list, binary_list, hexadecimal_list):
    print(f'{d} \"----\"  {b}  \"----\" + {h}')
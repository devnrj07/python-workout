# Differt types of Lists program

num_strings: list = ['15','100','55','42']
num_ints: list = [15,100,55,42]
num_floats : list = [1.5,100.1, 5.5,42.4]
num_lists : list = [[1,2,3],[4,5,6],[7,8,9]]

print('\n Summary')
print(f'\n The variable num_string is a {type(num_strings)}')
print(f'\n It contains the elements : {num_strings}')
print(f'\n The element {num_strings[0]} is a {type(num_strings[0])}')

print(f'\n The variable num_ints is a {type(num_ints)}')
print(f'\n It contains the elements : {num_ints}')
print(f'\n The element {num_ints[0]} is a {type(num_ints[0])}')

print(f'\n The variable num_floats is a {type(num_floats)}')
print(f'\n It contains the elements : {num_floats}')
print(f'\n The element {num_floats[0]} is a {type(num_floats[0])}')

print(f'\n The variable num_lists is a {type(num_lists)}')
print(f'\n It contains the elements : {num_lists}')
print(f'\n The element {num_lists[0]} is a {type(num_lists[0])}')

print('\n Now sorting num_ints and num_strings')
sorted_num_strings = sorted(num_strings)
print(f'\n sorted num_strings {sorted_num_strings}')
sorted_num_ints = sorted(num_ints)
print(f'\n sorted num_ints {sorted_num_ints}')
print(f'\n strings are sorted alphabatically while nums are sorted numerically!')

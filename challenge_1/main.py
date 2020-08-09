# count occurence of a specific letter

name=input('Hi! What is your name ?: ')

sentence = input(f'\nHi {name}, type a big sentence.: ')

letter_to_be_counted = input('\nwhich letter count do you need ? enter only single character: ')

input_length = len(letter_to_be_counted.strip().split())

if (input_length > 1):
    print('\nToo many letters. Enter only one letter.')

count_of_letter = sentence.lower().count(letter_to_be_counted.lower())

print(f'\nHi {name}, {letter_to_be_counted} occurs {count_of_letter} times in {sentence}')
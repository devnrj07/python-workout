# Frequency Analysis App
from collections import Counter
print('\n Welcome the Frequency Analysis app.')


def analyse_phrase():
    # List of elements to remove from all text for analysis
    non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ',
                   '.', '?', '!', ',', '"', "'", ':', ';', '(', ')', '%', '$', '&', '#', '\n', '\t']

    user_phrase_1 = input('\nEnter a phrase to be analyzed : ').lower().strip()

    for character in non_letters:
        user_phrase_1 = user_phrase_1.replace(character,'')

    total_occurences = len(user_phrase_1)
    letter_count = Counter(user_phrase_1)

    print("\nHere is the frequency analysis from key phrase 1: ")
    print("\n\tLetter\t\tOccurrence\tPercentage")
    # Result
    for char, count in sorted(letter_count.items()):
        print(
            f'\n Character : {char}\t\t count : {count} \t\t % : {round((count/total_occurences)*100)}')

    #Make a list of letters from highest occurrence to lowest
    ordered_letter_count = letter_count.most_common()
    user_phrase_1_ordered_letters = []
    for pair in ordered_letter_count:
        user_phrase_1_ordered_letters.append(pair[0])
    
    #Print the list
    print("\nLetters ordered from highest occurrence to lowest: ")
    for letter in user_phrase_1_ordered_letters:
        print(letter, end='')

analyse_phrase()
analyse_phrase()
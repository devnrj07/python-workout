#Guess My world app
import random

"""
You are responsible for writing a program that plays a word guessing game with a user. Your
program will provide a category of words to the user and a string of dashes “-----” that represent
the length of the word. The user will guess the word and with each incorrect guess, your
program will reveal a letter at random, “-a---”. Upon guessing the word correctly, your program
will then inform the user how many guesses they took.
"""

print('\n Welcome to the Guess My world app.')

game_dict = {
    'sports':['basketball', 'baseball', 'cricket', 'football', 'golf', 'tennis', 'hockey'],
    'colors':['blue', 'red', 'yellow', 'violet', 'magenta', 'green'],
    'movies':['halo', 'elysium', 'speed', 'nightcrawler', 'one', 'lost', 'focus'],
    'fruits':['apple', 'banana', 'orange', 'mango', 'strawberry', 'kiwi', 'grapes']
}

game_keys = list(game_dict.keys())
active = True

while active:
    game_category = game_keys[random.randint(0,len(game_keys)-1)]
    game_word = game_dict[game_category][random.randint(0,len(game_dict[game_category])-1)]
    word_length = len(list(game_word))
    blank_word = list()
    for i in range(0, word_length):
        blank_word.append('-')
    print(f'\n Guess the word which belongs to {game_category} category and has {word_length} letters')
    guess=""
    guess_count = 0
    while guess != game_word:
        blank_word_list = ' '.join(blank_word)
        print(f'\n Word to guess {blank_word_list}')
        guess = input('\n make a guess :').lower()
        guess_count +=1
        if guess_count == word_length - 2:
            print(f'\n Too many guesses. correct word is {game_word}. Thank you for playing with us.')
            break

        if guess ==  game_word:
            print(f'\n You won the game!! You took {guess_count} chances.')
            break
        else:
            print('\n Oops! That\'s a wrong guess. Try Again. ')
            running=True
            while running:
                letter_index = random.randint(0,word_length-1)
                if blank_word[letter_index] == '-':
                    blank_word[letter_index] = game_word[letter_index]
                    running=False

        continue_program = input('\n Do you want to try again ? (y/n) : ').lower().strip()
        if continue_program.startswith('n'):
            active = False
            print('\n Have a nice day!')            

    continue_program = input('\n Do you want to play again ? (y/n) : ').lower().strip()
    if continue_program.startswith('n'):
            active = False
            print('\n Have a nice day!')            



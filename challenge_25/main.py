#Code Breaker App - Extension of Frequnecy analysis app
from collections import Counter
"""
RULES 
You should be able to encode or decode a message regardless of the key phrases
chosen.
To In order to accomplish this, you must look at the frequency analysis of the two key
phrases.
Given a character in the secret message that is to be encoded, you must find its index in
the frequency analysis of the first message.
Then find the letter that appears at the same index in the frequency analysis of the
second message.
This is your encoding rule to encode one character as another.
For example, the letter "o" appears at index 1 in the first frequency analysis. The letter "t"
appears at index 1 in the second frequency analysis. Therefore the letter “o” would be
encoded to the letter “t”.
The letter “h” appears at index 7 in the first frequency analysis. The letter “r” appears at
index 7 in the second frequency analysis. Therefore the letter “h” would be encoded to
the letter “r”.
Similarly, the word “oh” would be encoded to “tr” using the given key phrases.
"""

def filter_non_letters(input_phrase:str):
    # List of elements to remove from all text for analysis
    non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '@'
                   '.', '?', '!', ',', '"', "'", ':', ';', '(', ')', '%', '$', '&', '#', '\n', '\t']

    user_phrase_1 = input_phrase.lower().strip()

    for character in non_letters:
        user_phrase_1 = user_phrase_1.replace(character,'')

    return user_phrase_1

def analyse_phrase(input_phrase:str):

    user_phrase_1 = filter_non_letters(input_phrase)
    
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

    return user_phrase_1_ordered_letters

PHRASE_1 = """
Quite so! You have not observed. And yet you have seen.
That is just my point. Now, I know that there are seventeen steps, because I
have both seen and observed.
By the way, since you are interested in these little problems,
and since you are good enough to chronicle one or two of my trifling
experiences, you may be interested in this.
He threw over a sheet of thick, pink tinted notepaper which had been lying open
upon the table.
It came by the last post, said he. Read it aloud.
The note was undated, and without either signature or address.
There will call upon you tonight, at a quarter to eight o'clock,
it said, "a gentleman who desires to consult you upon a matter of the very
deepest moment.
Your recent services to one of the royal houses of Europe have shown that you
are one who may safely be trusted
with matters which are of an importance which can hardly be exaggerated.
This account of you we have from all quarters received.
Be in your chamber then at that hour, and do not take it amiss if your visitor
wear a mask.
This is indeed a mystery, I remarked. What do you imagine that it means?
I have no data yet. It is a capital mistake to theorise before one has data.
Insensibly one begins to twist facts to suit theories, instead of theories to
suit facts.
But the note itself. What do you deduce from it?
I carefully examined the writing, and the paper upon which it was written.
The man who wrote it was presumably well to do, I remarked, endeavouring to
imitate my companion's processes.
Such paper could not be bought unde
"""

PHRASE_2 = """
To Sherlock Holmes she is always the woman. I have seldom heard him mention her
under any other name.
In his eyes she eclipses and predominates the whole of her sex. It was not that
he felt any emotion akin to love for Irene Adler.
All emotions, and that one particularly, were abhorrent to his cold, precise but
admirably balanced mind.
He was, I take it, the most perfect reasoning and observing machine that the
world has seen,
but as a lover he would have placed himself in a false position.
He never spoke of the softer passions, save with a gibe and a sneer.
They were admirable things for the observer excellent for drawing the veil from
men's motives and actions.
But for the trained reasoner to admit such intrusions into his own delicate and
finely adjusted temperament was to introduce
a distracting factor which might throw a doubt upon all his mental results.
Grit in a sensitive instrument, or a crack in one of his own highpower lenses,
would not be more disturbing than a strong emotion in a nature such as his.
And yet there was but one woman to him, and that woman was the late Irene Adler,
of dubious and questionable memory.
I had seen little of Holmes lately. My marriage had drifted us away from each
other.
My own complete happiness, and the homecentred interests which rise up around
the man who first finds himself master of his own establishment,
were sufficient to absorb all my attention, while Holmes, who loathed every form
of society with his whole Bohemian soul,
remained in our lodgings in Baker Street, buried among his old books, and
alternating from week to week between cocaine and ambition,
the drowsiness of the drug, and the fierce energy of his own keen nature.
He was still, as ever, deeply attracted by the study of crime,
and occupied his immense faculties and extraordinary powers of observation in
following out those clues,
and clearing up those mysteries which had been abandoned as hopeless by the
official police.
From time to time I heard some vague account of his doings: of his summons to
Odessa in the case of the Trepoff murder,
of his clearing up of the singular tragedy of the Atkinson brothers at
Trincomalee,
and finally of the mission which he had accomplished so delicately and
successfully for the reigning family of Holland.
Beyond these signs of his activity, however, which I merely shared with all the
readers of the daily press,
I knew little of my former friend and companion.
"""


def main_app ():
    print('\n Welcome to the Code Breaker App')
    
    ordered_phrase_one = analyse_phrase(PHRASE_1)
    ordered_phrase_two = analyse_phrase(PHRASE_2)
    
    user_response = input('\n Would You like to encode or decode : (e/d) ').lower().strip()
    message_from_user = input('\n Enter your message. : ').lower().strip()

    #filter user message
    filtered_message = filter_non_letters(message_from_user)

    encoded_list = list()
    decoded_list = list()

    if user_response.startswith('e'):
        for letter in filtered_message:
            index = ordered_phrase_one.index(letter)
            letter = ordered_phrase_two[index]
            encoded_list.append(letter)

        print('\n Encoded message :')
        for letter in encoded_list:
            print(letter, end='')    

    elif user_response.startswith('d'):
        for letter in filtered_message:
            index = ordered_phrase_two.index(letter)
            letter = ordered_phrase_one[index]
            decoded_list.append(letter)

        print('\n Decoded message : ')
        for letter in decoded_list:
            print(letter, end='')    
    else:
        print('\n Well, that\'s an invalid selection.')

main_app()
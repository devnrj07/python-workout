#Thesaurus App
import random

print('\n Welcome to the thesaurus app')
thesaurus = {
    'pride':['honour','dignity','delight','joy','self-esteem'],
    'prejudice':['harm', 'preconception', 'detriment', 'damage','sway'],
    'stoic': ['stoical','hardship','emotionalless','controlled-feeling','lonewolf'],
    'insular':['isolated','blinkered','inaccessible','segregated','boring'],
    'wry':['ironic','sardonic','satirical','sneering','evil'],
    'belligerent':['hostile','aggresive','threatening', 'antagonistic','pugnacious'],
    'allure':['attractive','pull','appeal','glamour','entice','tempt']
}

print('\n Available keywords')
for key in thesaurus:
    print(f'\n {key}')
word = input('\n Pick a word you want synonym for : ').lower()
random_no = random.randint(0,4)
if word in thesaurus:
    print(f'\n Synonym  for {word} is {thesaurus[word][random_no]}')
    response = input('\n Would you like to see complete thesaurus ? (y/n) ').lower().strip()
    if response == 'y':
        for key, values in thesaurus.items():
            print(f'\n Word {key} is synonym to : ')
            for value in values:
                print(f'\n - {value}')
    else:
        print('\n Goodbye! Have a nice day.')    
else:
    print(f'\n {word} doesn\'t exist!')    
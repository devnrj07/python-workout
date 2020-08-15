# Coin Toss App
import random

print('\n Welcome to the coin toss app.')

coin_toss_no = int(input('\n Enter ther number of times you want to flip the coin ? '))
display_each_toss_result = input('\n Do you want to see result of each toss ? (y/n) ').lower()

heads_count = 0
tails_count = 0

print('\n Flipping !!')

for i in range(1,coin_toss_no+1):
    result = random.randint(0,1)
    if 'y' in display_each_toss_result:
        if result == 0 :
            print('\n Heads!')
        else:
            print('\n Tails!')    

    if result == 0:
        heads_count +=1
    elif result == 1:
        tails_count +=1

    if heads_count == tails_count:
        print(f'\n Oh! At toss {i}, heads equals tails with {heads_count} each ')

head_percent = round((heads_count/coin_toss_no) *100,2)
tail_percent = round((tails_count/coin_toss_no) *100,2)

print('\n Summary report....')
print('\n Side \t\t Count \t\t Percentage ')
print(f'\n Head \t\t {heads_count} \t\t {head_percent}')
print(f'\n Tail \t\t {tails_count} \t\t {tail_percent}')
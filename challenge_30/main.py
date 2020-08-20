#Power ball simulation App
import random

print('\n Welcome to the power ball App.')
white_balls=int(input('\n Enter the white ball number : '))
red_balls=int(input('\n Enter the red ball number : '))

if white_balls  < 6:
    white_balls = 5
if red_balls < 2:
    red_balls = 1

odds = 1

for i in range(5):
    odds *= white_balls-1

#red balls
odds *= red_balls/120

print(f'\n odds of your winning with {white_balls} white balls and {red_balls} red_balls are : {odds}')

ticket_interval = int(input('\n How many tickets would you like to purchase ? '))

winning_numbers = list()
while len(winning_numbers) < 5:
    white_ball_no = random.randint(1,white_balls)
    if white_ball_no not in winning_numbers:
        winning_numbers.append(white_ball_no)
winning_numbers.sort()

#red ball no
red_ball_no = random.randint(1,red_balls)
winning_numbers.append(red_ball_no)

print('\n Welcome to the Power ball Game')
print(f'\n Winning balls are : {winning_numbers}',end='')
input('\n Press Enter to purchase the tickets')

tickets_purchased=0
playing=True
tickets_sold = []

while winning_numbers not in tickets_sold and playing == True:
    lottery_numbers = []
    while len(lottery_numbers) < 5:
        number = random.randint(1,white_balls)
        if number not in lottery_numbers:
            lottery_numbers.append(number)
    lottery_numbers.sort()

    number = random.randint(1,red_balls)
    lottery_numbers.append(number)

    #Tickets that have not been sold
    if lottery_numbers not in tickets_sold:
        tickets_purchased+=1
        tickets_sold.append(lottery_numbers)
        print(lottery_numbers)
    else:
        print('\n Losing ticket generated. disregard....')

    if tickets_purchased % ticket_interval == 0:
        print(str(tickets_purchased) + " tickets purchased so far with no winners...")
        choice = input("\nKeep purchasing tickets (y/n): ")
        if choice != 'y':
            playing = False        
    
#The lottery is now over
#We purchased the winning ticket and we won the lottery
if lottery_numbers == winning_numbers:
    print("\nWinning ticket numbers: ", end='')
    for number in lottery_numbers:
        print(str(number), end=' ')
        print("\nPurchased a total of " + str(tickets_purchased) + " tickets.")
#We didn't purchase the winning ticket and we gave up
else:
    print("\nYou bought " + str(tickets_purchased) + " tickets and still lost!")
    print("Better luck next time!")    

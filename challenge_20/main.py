#Rock, paper scissor app
import random
print('\nWelcome to Rock, Scissors, and papper app.')

rounds = int(input('\n How many rounds would you like to play ? '))
moves = ['scissors', 'rock', 'paper']

user_score = 0 
AI_score = 0

for round in range(rounds):
    message = ""
    winner = ""

    print('\nRound \t\t player score \t\t AI score ')
    print(f'\n {round+1} \t\t {user_score} \t\t {AI_score}')

    AI_choice = random.choice(moves)
    user_choice = input('\n Enter your choice rock, paper, scissors : ').lower().strip()

    if user_choice in moves:
        print(f'\n AI_picked {AI_choice} and you picked {user_choice} ')
        #AI choses scissors
        if AI_choice == 'scissors' and user_choice == 'scissors':
            message = "Scissors cut Scissors!"
            winner = "tie"
        elif AI_choice == 'scissors' and user_choice == 'paper':
            message = "Scissors cut paper!"
            winner = "AI"
        elif AI_choice == 'scissors' and user_choice == 'rock':
            message = "Rock smashed scissors!"
            winner = "Player"
        
        #AI choses Rock    
        elif AI_choice == 'rock' and user_choice == 'rock':
            message = "Rock smashes Rock!"
            winner = "tie"
        elif AI_choice == 'rock' and user_choice == 'scissors':
            message = "Rock smashed Scissors"
            winner= "AI"
        elif AI_choice == 'rock' and user_choice == 'paper':
            message = "Paper wraps the rock!"
            winner = "Player"
        #AI choses Paper    
        elif AI_choice == 'paper' and user_choice == 'paper':
            message = "Paper does nothing to paper!"
            winner = "tie"
        elif AI_choice == 'paper' and user_choice == 'scissors':
            message = "Scissors cut paper into pieces!"
            winner = "Player"
        elif AI_choice == 'paper' and user_choice == 'rock':
            message = "Paper wraps rock!"
            winner = "AI"
        else:
            print("Round not calculated")
            winner = "tie"                           
            message = "It's a tie how boring"

        print(f'\n\t {message} ')
        if winner == 'Player':
            print(f'\t Player wins the round {round+1}')
            user_score +=1
        elif winner == 'AI':
            print(f'\t AI wins the round {round+1}')
            AI_score +=1
        else:
            print('\t This round is a tie')
    else:
        print("That is not a valid game option!")
        print("Computer gets the point!")
        AI_score += 1        

#Game ended print the results
print("\nFinal Game Results")
print(f"\tRounds Played: {rounds}")
print(f"\tPlayer Score: {user_score}")
print(f"\tAI Score: {AI_score}")
if user_score > AI_score:
    print("\tWinner: PLAYER!!!")
elif AI_score > user_score:
    print("\tWinner: AI :-(")
else:
    print("\tThe game was a tie.")
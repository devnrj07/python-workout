import random
# Pythonagachi Simulator app
'''
You will be responsible for writing a program that simulates the behavior of a retro 90’s
Tamagachi toy. You program will allow a user to create their own creature, give it a name, and
care for it until it unfortunately parishes. Users will monitor the creatures hunger, boredom,
tiredness, and dirtiness and take actions to prevent any of the categories from getting to high. If
the categories get too high there will be unfortunate consequences.
'''

class Creature:

    def __init__(self,name):
        self.name = name
        self.boredom = 0
        self.hunger = 0
        self.tiredness = 0
        self.dirtiness = 0
        self.food = 2
        self.is_sleeping = False
        self.is_alive = True

    def eat(self):
        if self.food > 0 :
            self.food -= 1
            self.hunger -= random.randint(1,4)
            print(f'\n {self.name} had a great lunch.')
        else:
            print(f'\n {self.name} has no food to eat.')    
        if self.hunger < 0 :
            self.hunger = 0

    def play(self):
        rand_int = random.randint(0,2)
        print(f'\n {self.name} wants to play game. \n It has choosen a number between (0 & 2)')        
        user_input = int(input('\n Guess a number between 0 and 2. '))
        if user_input == rand_int :
            print(f'\n Yay! You guessed it correct.')
            self.boredom -=3
        else :
            print('\n Oops! That was a wrong guess. ')
            self.boredom -= 1    
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        self.is_sleeping = True 
        self.tiredness -= 3
        self.boredom -= 2
        print('\n Creature is sleeping zzz...') 
        if self.boredom < 0:
            self.boredom = 0
        if self.tiredness < 0:
            self.tiredness = 0              

    def awake(self):
        rand_int = random.randint(0,2)
        if rand_int == 0:
            print('\n Creature Just Woke up. ')
            self.is_sleeping = False
            self.boredom = 0
        else :
            print('\n creature won\'t wake up')
            self.sleep()

    def clean(self):
        self.dirtiness = 0
        print(f'\n {self.name} just took a bath. ')

    def forage(self):
        food_found = random.randint(0,4)
        self.food+=food_found
        self.dirtiness +=2
        print(f'\n {self.name} found  {food_found} amount of food. ')

    def show_values(self):
        print(f'\n {self.name} has the following Stats :')
        print(f'\n Hunger : {self.hunger} ')
        print(f'\n Boredom : {self.boredom} ')
        print(f'\n Tirediness : {self.tiredness} ')
        print(f'\n Dirtiness : {self.dirtiness}')
        print(f'\n Food Inventory : {self.food} ')
        print(f'\n Sleeping Status : {self.is_sleeping}')

    def increment_value(self, difficulty):
        self.hunger += random.randint(0,difficulty)
        if self.is_sleeping == False:
            self.boredom += random.randint(0,difficulty)
            self.tiredness += random.randint(0,difficulty)
        self.dirtiness += random.randint(0,difficulty)

    def kill(self):
        if self.hunger >= 10 :
            print(f'\n {self.name} creature starved to death. ')
            self.is_alive = False                                        
        elif self.dirtiness >= 10:
            print(f'\n {self.name} suffered an infection and died. ')
            self.is_alive = False 
        elif self.boredom >= 10:
            self.boredom = 10
            print(f'\n {self.name} creature is feeling bored and falling asleep. ')
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print(f'\n {self.name} creature is sleepy and falling asleep. ')
            self.is_sleeping = True

def show_menu(creature:Creature):
    if creature.is_sleeping:
        user_choice = input('\n Creature is sleeping. What do you wanna do ? ')
        user_choice = '6'
        return user_choice
    else :
        user_choice = input('\n Select one option. \n Enter 1 to eat. \n Enter 2 to play.\n Enter 3 to sleep.\n Enter 4 to take bath.\n Enter 5 to forage. ')
        return user_choice                   

def call_action(creature:Creature, choice:str):
    methods = {
        '1': creature.eat,
        '2': creature.play,
        '3': creature.sleep,
        '4': creature.clean,
        '5': creature.forage,
        '6': creature.awake,
        
    }
    func = methods.get(choice, lambda: 'Incorrect selection.')
    return func()
if __name__ == "__main__":
    print('Welcome to 90\'s game. ')
    difficulty = int(input('Please choose difficulty(1-5). '))
    if difficulty > 5 :
        difficulty = 5
    elif difficulty < 1 :
        difficulty = 1
    active = True
    while active:
        name = input('\n Enter you creature\'s name. ')
        player = Creature(name)
        round = 1
        while player.is_alive:
            print(f'# This is round {round}')
            player.show_values()
            option = show_menu(player)
            call_action(player,option)

            print('Round one summary :')
            player.show_values()
            input('Press Enter to continue. ')

            player.increment_value(difficulty)
            player.kill()
            round +=1
        print(f'R.I.P {name}. ')
        print(f'{name} survived {round} rounds .')
        play_again = input('Do You wanna play again (y/n) ? ')                        

        if 'n' in play_again.lower():
            active = False
    print('Thank you playing.')         
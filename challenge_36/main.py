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
            print(f'{self.name} had a great lunch.')
        else:
            print(f'{self.name} has no food to eat.')    
        if self.hunger < 0 :
            self.hunger = 0

    def play(self):
        rand_int = random.randint(0,2)
        print(f'{self.name} wants to play game. \n It has choosen a number between (0 & 2)')        
        user_input = int(input('Guess a number between 0 and 2. '))
        if user_input == rand_int :
            print(f'Yay! You guessed it correct.')
            self.boredom -=3
        else :
            print('Oops! That was a wrong guess. ')
            self.boredom -= 1    
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        self.is_sleeping = True 
        self.tiredness -= 3
        self.boredom -= 2
        print('Creature is sleeping zzz...') 
        if self.boredom < 0:
            self.boredom = 0
        if self.tiredness < 0:
            self.tiredness = 0              

    def awake(self):
        rand_int = random.randint(0,2)
        if rand_int == 0:
            print('Creature Just Woke up. ')
            self.is_sleeping = False
            self.boredom = 0
        else :
            print('creature won\'t wake up')
            self.sleep()

    def clean(self):
        self.dirtiness = 0
        print(f'{self.name} just took a bath. ')

    def forage(self):
        food_found = random.randint(0,4)
        self.food+=food_found
        self.dirtiness +=2
        print(f'{self.name} found  {food_found} amount of food. ')

    def show_values(self):
        print(f'\n {self.name} has the following Status :')
        print(f'\n Hunger : {self.hunger} ')
        print(f'\n Boredom : {self.boredom} ')
        print(f'\n Tirediness : {self.tiredness} ')
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
            print(f'{self.name} creature starved to death. ')
            self.is_alive = False                                        
        elif self.dirtiness >= 10:
            print(f'{self.name} suffered an infection and died. ')
            self.is_alive = False 
        elif self.boredom >= 10:
            self.boredom = 10
            print(f'{self.name} creature is feeling bored and falling asleep. ')
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print(f'{self.name} creature is sleepy and falling asleep. ')
            self.is_sleeping = True

                   
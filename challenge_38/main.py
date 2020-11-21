# Pykemon Simulation App
'''
You will be responsible for writing a program the emulates playing the hit game Pokemon. Your
program will generate Pykemon creatures randomly. Each Pykemon creature will be one of
three different elemental types: fire, water, or grass. Each Pykemon type will have its own set
of unique moves and each individual Pykemon will have it’s one name, health stat, and speed
stat.You will be given one Pykemon and then be tasked with fighting other pykemon until you
run out of health. In the original Pokemon, the user is presented with three Pokemon to choose
from at the start of the game; one of each elemental type. Pykemon is no different. You will
choose your starting Pykemon and then be off on a journey to battle other wild Pykemon until
your Pykemon faints.
'''
import random


class Pykemon():
    def __init__(self, name, element, health, speed):
        self.name = name.title()
        self.element = element
        self.current_health = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True

    def light_attack(self, enemy):
        damage = random.randint(15, 25)
        print(f'Pykemon {self.name} used {self.moves[0]}. ')
        print(f'It dealt {damage} damage.')
        enemy.current_health -= damage

    def heavy_attack(self, enemy):
        damage = random.randint(0, 50)
        print(f'Pykemon {self.name} used {self.moves[1]}. ')
        if damage < 10:
            print(f'It dealt no damage.')
        else:
            print(f'It dealt {damage} damage.')
            enemy.current_health -= health

    def restore(self):
        heal = random.randint(15, 25)
        print(f'Pykemon {self.name} used {self.moves[2]}. ')
        print(f'It healed itself by {heal} points. ')
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def faint(self):
        if self.current_health <= 0:
            self.is_alive = False
            print('f {self.name} has fainted. ')
            input('Press Enter to continue. ')

    def show_stats(self):
        print(f' Name : {self.name}.')
        print(f' Type : {self.element}.')
        print(
            f'Current Health : {self.current_health} and Max Health : {self.max_health}. ')
        print(f'Speed : {self.speed}.')


class Fire(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['Scratch', 'Ember', 'Light', 'Fire Blast']

    def special_attack(self, enemy: Pykemon):
        print(f'{self.name} performed {self.moves[3]} task. ')
        if enemy.type == 'GRASS':
            print(f'The move was super effective and dealt heavy damage. ')
            damage = random.randint(35, 50)
        if enemy.type == 'WATER':
            print(f'The move was not effective and dealt little damage. ')
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        print(f'It dealt {damage} damage.')
        enemy.current_health -= damage

    def move_info(self):
        print(f'\n{self.name} moves : ')
        print(f'\n--{self.moves[0]}--')
        print(f'\n An efficient attack...')
        print(f'\n Guaranteed to do damage within the range of 15 to 25 damage points.')

        print(f'\n--{self.moves[1]}--')
        print(f'\n A risky attack......')
        print(f'\n Could deal up to 50 damage points or as little as 0 damage points.')

        print(f'\n--{self.moves[2]}--')
        print(f'\n A restorative move...')
        print(f'\n Guaranteed to heal your Pykemon 15 to 25 health points.')

        print(f'\n--{self.moves[3]}--')
        print(f'\n A powerful FIRE based attack...')
        print(f'\n Guaranteed to deal MASSIVE damage to GRASS type Pykemon.')


class Water(Pykemon):
    def __init(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['Bite', 'Splash', 'Dive', 'Water Cannon']

    def special_attack(self, enemy: Pykemon):
        print(f'{self.name} performed {self.moves[3]} task. ')
        if enemy.type == 'FIRE':
            print(f'The move was super effective and dealt heavy damage. ')
            damage = random.randint(35, 50)
        if enemy.type == 'GRASS':
            print(f'The move was not effective and dealt little damage. ')
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        print(f'It dealt {damage} damage.')
        enemy.current_health -= damage

    def move_info(self):
        print(f'\n{self.name} moves : ')
        print(f'\n--{self.moves[0]}--')
        print(f'\n An efficient attack...')
        print(f'\n Guaranteed to do damage within the range of 15 to 25 damage points.')

        print(f'\n--{self.moves[1]}--')
        print(f'\n A risky attack......')
        print(f'\n Could deal up to 50 damage points or as little as 0 damage points.')

        print(f'\n--{self.moves[2]}--')
        print(f'\n A restorative move...')
        print(f'\n Guaranteed to heal your Pykemon 15 to 25 health points.')

        print(f'\n--{self.moves[3]}--')
        print(f'\n A powerful FIRE based attack...')
        print(f'\n Guaranteed to deal MASSIVE damage to GRASS type Pykemon.')


class Grass(Pykemon):
    def __init(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ['Vine whip', 'Wrap', 'Grow', 'Leaf Blade']

    def special_attack(self, enemy: Pykemon):
        print(f'{self.name} performed {self.moves[3]} task. ')
        if enemy.type == 'WATER':
            print(f'The move was super effective and dealt heavy damage. ')
            damage = random.randint(35, 50)
        if enemy.type == 'FIRE':
            print(f'The move was not effective and dealt little damage. ')
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        print(f'It dealt {damage} damage.')
        enemy.current_health -= damage

    def move_info(self):
        print(f'\n{self.name} moves : ')
        print(f'\n--{self.moves[0]}--')
        print(f'\n An efficient attack...')
        print(f'\n Guaranteed to do damage within the range of 15 to 25 damage points.')

        print(f'\n--{self.moves[1]}--')
        print(f'\n A risky attack......')
        print(f'\n Could deal up to 50 damage points or as little as 0 damage points.')

        print(f'\n--{self.moves[2]}--')
        print(f'\n A restorative move...')
        print(f'\n Guaranteed to heal your Pykemon 15 to 25 health points.')

        print(f'\n--{self.moves[3]}--')
        print(f'\n A powerful FIRE based attack...')
        print(f'\n Guaranteed to deal MASSIVE damage to GRASS type Pykemon.')


class Game():
    def __init__(self):
        self.pykemon_elements = ['FIRE', 'WATER', 'GRASS']
        self.pykemon_names = ['Chewdie', 'Spatol', 'Burnmander', 'Pykachu', 'Pyonx', 'Abbacab', 'Sweetil',
                              'Jampot', 'Hownstooth', 'Swagilybo', 'Muttle', 'Zantbat', 'Wiggly Poof', 'Rubblesaur', ]
        self.battles_won = 0

    def create_pykemon(self):
        health = random.randint(70, 100)
        speed = random.randint(1, 10)
        element = self.pykemon_elements[random.randint(
            0, len(self.pykemon_elements)-1)]
        name = self.pykemon_names[random.randint(0, len(self.pykemon_names)-1)]

        if element == 'FIRE':
            pykemon = Fire(name, element, health, speed)
        if element == 'WATER':
            pykemon = Water(name, element, health, speed)
        if element == 'GRASS':
            pykemon = Grass(name, element, health, speed)

        return pykemon

    def choose_pykemon(self):
        starters = []
        while len(starters) < 3:
            Pykemon = self.create_pykemon()
            valid_pykemon = True
            for starter in starters:
                if starter.name == Pykemon.name or starter.element == Pykemon.element:
                    valid_pykemon = False
            if valid_pykemon:
                starters.append(Pykemon)
            for starter in starters:
                starter.show_stats()
                starter.move_info()
            print("\nProfessor Eramo presents you with three Pykemon: ")
            print("(1) - " + starters[0].name)
            print("(2) - " + starters[1].name)
            print("(3) - " + starters[2].name)

            choice = int(input("Which Pykemon would you like to choose: "))
            Pykemon = starters[choice-1]

            return Pykemon

    def get_attack(self, pykemon):
        print("\nWhat would you like to do...")
        print("(1) - " + pykemon.moves[0])
        print("(2) - " + pykemon.moves[1])
        print("(3) - " + pykemon.moves[2])
        print("(4) - " + pykemon.moves[3])
        choice = int(input("Please enter your move choice: "))
        # Formatting
        print()
        print(
            "-----------------------------------------------------------------------------")
        return choice

    def player_attack(self, move, player, computer):
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)
        # Check to see if the computer has fainted
        computer.faint()

    def computer_attack(self, player, computer):
        move = random.randint(1, 4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)
        player.faint()

    def battle(self, player, computer):
        move = self.get_attack(player)
        if player.speed >= computer.speed:
            self.player_attack(move, player, computer)
            if computer.is_alive:
                self.computer_attack(player, computer)
        else:
            self.computer_attack(player, computer)
            if player.is_alive:
                self.player_attack(move, player, computer)


if __name__ == "__main__":
    print("Welcome to Pykemon!")
    print("Can you become the worlds greatest Pykemon Trainer???")
    print("\nDon't worry! Prof Eramo is here to help you on your quest.")
    print("He would like to gift you your first Pykemon!")
    print("Here are three potential Pykemon partners.")
    input("Press Enter to choose your Pykemon!")

    playing_main = True
    while playing_main:
        game = Game()
        player = game.choose_pykemon()
        print("\nCongratulations Trainer, you have chosen " + player.name + "!")
        input("\nYour journey with " + player.name +
              " begins now...Press Enter!")

        # While your pykemon is alive, continue to do battle
        while player.is_alive:
            # Create a computer pykemon to battle
            computer = game.create_pykemon()
            print("\nOH NO! A wild " + computer.name + " has approached!")
            computer.show_stats()
            while computer.is_alive and player.is_alive:
                game.battle(player, computer)
                # Both parties survived a round, show their current stats
                if computer.is_alive and player.is_alive:
                    player.show_stats()
                    computer.show_stats()
    # Formatting
    print("-----------------------------------------------------------------------------")
    if player.is_alive:
        game.battles_won += 1

    # The player has finally fainted
    print("\nPoor " + player.name + " has fainted...")
    print("But not before defeating " + str(game.battles_won) + " Pykemon!")
    # Ask the user if they want to play again
    choice = input("Would you like to play again (y/n): ").lower()
    if choice != 'y':
        playing_main = False
        print("Thank you for playing Pykemon!")

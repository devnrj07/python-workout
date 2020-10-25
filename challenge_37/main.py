# Casino Black Jack App

'''
You are responsible for writing a program that allows a user to play casino Black Jack. The
user will put a set amount of money onto the table and make a minimum $20 bet each hand.
Each hand, the user will be dealt two cards and be given the option to hit or stay. If the user hits
21 or goes over the round will end. The dealer will continue to hit until their hand has a
minimum value of 17 as per casino guidelines. The user will be able to play as long as their
total money is greater than or equal to the minimum bet of the table.
'''
import random
import time


class Card:
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit

    def display_card(self):
        print(f'{self.rank} of {self.suit}. ')


class Deck:
    def __init__(self):
        self.cards = []

    def build_deck(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                    '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, }
        for suit in suits:
            for key, value in ranks.items():
                card = Card(key, value, suit)
                self.cards.append(card)
    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck:Deck):
        for i in range(0,2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        print('Printing player\'s hand. ')
        for card in self.hand:
            card.display_card()

    def hit(self, deck: Deck):
        card = deck.deal_card()
        self.hand.append(card)

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value 
            if card.rank == 'A':
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand == True:
                self.hand_value -= 10
        print(f'\n Player\'s Hand value {self.hand_value}.')                   

    def update_hand(self, deck : Deck):
        if self.hand_value < 21:
            hit = input('Would you like to hit ? (y/n) ')
            if 'y' in hit.lower():
                self.hit(deck)
            else :
                self.playing_hand = False
        else :
            self.playing_hand = False
                                    
class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True
    
    def draw_hand(self, deck:Deck):
        for i in range(0,2):
            card = deck.deal_card()
            self.hand.append(card)

    def display_hand(self):
        input('\n Press Enter to reveal dealers cards')
        for card in self.hand:
            card.display_card()
            time.sleep(1)

    def hit(self, deck: Deck):
        self.get_hand_value()
        if self.hand_value < 17 :        
            card = deck.deal_card()
            self.hand.append(card)
            self.get_hand_value()
        print(f'Dealer has {len(self.hand)} cards in hand. ')

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        for card in self.hand:
            self.hand_value += card.value 
            if card.rank == 'A':
                ace_in_hand = True
        if self.hand_value > 21 and ace_in_hand == True:
                self.hand_value -= 10
                         
        

class Game:
    def __init__(self,money):
        self.money = money
        self.bet = 20
        self.winner = ''

    def set_bet(self):
        betting = True
        while betting:
            bet = int(input('\n Place your bet or Press (q) to Quit : '))    
            if bet < 20 :
                self.bet = 20
            elif bet > self.money:
                print('Sorry! You don\'t have enough money. ')
            elif bet == int('q'):
                print('\n Thank you for playing. ')
                break
            else :
                self.bet = bet 
                betting = False       

    def scoring(self, player_hand_value, dealer_hand_value):
        if player_hand_value == 21 :
            print('\n Yo! you just hit jackpot. ')
            self.winner = 'p'
        elif dealer_hand_value == 21 :
            print('\n They got black jack. ')
            self.winner = 'd'
        elif player_hand_value > 21:
            print('Oops! You went above 21. They Won!')
            self.winner = 'd'
        elif dealer_hand_value < 21 :
            print('The dealer went over 21. ')
            self.winner = 'p'
        else :
            if player_hand_value > dealer_hand_value :
                # print summary
                self.winner = 'p'
            elif player_hand_value < dealer_hand_value :
                # print summary
                self.winner = 'd'
            else :
                # tie print summary
                self.winner = 'tie'
    def payout(self):
        if self.winner == 'p':
            self.money += self.bet
        elif self.winner == 'd' :
            self.money -= self.bet 

    def display_money(self):
        print(f'\n Current Money : ${self.money} ')

    def display_money_and_bet(self):
        print(f'\nCurrent Money : ${self.money} and bet : ${self.bet} ')                                                               

if __name__ == "__main__":
    print('\n Welcome to the Black Jack App. ')
    print('\n Rule : Minimum bets $20 ')
    money = int(input('\n How much money do you wanna put on table ? '))
    game = Game(money)
    active = True
    while active:
        game_deck = Deck()
        game_deck.build_deck()
        game_deck.shuffle_deck()

        player = Player()
        dealer = Dealer()

        game.display_money()
        game.set_bet()

        player.draw_hand(game_deck)
        dealer.draw_hand(game_deck)

        game.display_money_and_bet()
        print(f'\n Dealer\'s first card : {dealer.hand[0].rank} of {dealer.hand[0].suit}')

        while player.playing_hand :
            player.display_hand()
            player.get_hand_value()
            player.update_hand(game_deck)

        dealer.hit(game_deck)
        dealer.display_hand()

        game.scoring(player.hand_value,dealer.hand_value)
        game.payout()

        if game.money < 20 :
            print('User exhausted the money! ')
            active = False    

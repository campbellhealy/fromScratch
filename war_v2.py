from random import shuffle
from os import system 
from time import sleep

class Card:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = [None, None,"2", "3", "4", "5", "6", "7", "8", 
              "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        """suit + value are ints"""
        self.value = value
        self.suit = suit

    def __lt__(self, card2):
        if self.value < card2.value:
            return True
        if self.value == card2.value:
            if self.suit < card2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, card2):
        if self.value > card2.value:
            return True
        if self.value == card2.value:
            if self.suit > card2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v
    
class Player:
   def __init__(self, name):
       self.wins = 0
       self.card = None
       self.name = name      
      
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()  
      
           
class Game:
    def __init__(self):
        system('cls')
        name1 = input("Player 1, Enter your name... \n")
        system('cls')
        sleep(0.5)
        name2 = input("Player 2, Enter your name... \n")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        print(f"{winner} wins this round!\n")
        sleep(2)
        system('cls')

    def draw(self, p1name, p1card, p2name, p2card):
        d = f"{p1name} draws {p1card}"
        e = f"{p2name} draws {p2card}\n"
        system('cls')
        print(d)
        sleep(0.2)
        print(e)

    def play_game(self):
        cards = self.deck.cards
        system('cls')
        print("\nThe War! Begins!\n")
        print(f'Ready! - { self.p1.name}\nReady! - {self.p2.name}\n\n')
        while len(cards) >= 2:
            choice = input("Press Enter to Play\nor \nPress 'q' to End the War!\n").lower()
            if choice == 'q':
                system('cls')
                print('Chicken!')
                sleep(0.3)
                system('cls')
                break
            p1card = self.deck.rm_card()
            p2card = self.deck.rm_card()
            p1name = self.p1.name
            p2name = self.p2.name
            self.draw(p1name, p1card, p2name, p2card)
            if p1card > p2card:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        system('cls')
        print(f"War! is over.\n\n{win} Wins!!!\n\n") #.format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie! \nNo-One "   

game = Game()
game.play_game()
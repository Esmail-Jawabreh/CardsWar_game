import random
from random import shuffle

# Two useful variables for creating Cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 J Q K A'.split()


# mycards = [(s, r) for s in SUITE for r in RANKS]
# mycards=[]
# for s in SUITE:
#     for r in RANKS:
#         mycards.append((s,r))


class Deck:
    """
    Deck Class:
    this object will create a deck of cards to initiate play.
    then you can use deck listof cards to split in half, and give to the players.
    it will use SUITE and RANKS to create the deck,
    it should also have a method for splitting / cutting the deck in half and suffling the deck.
    """

    def __init__(self):
        print("Creating a new ordered Deck ..")
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("shuffling deck ..")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    """
    Hand Class:
    each playes has a hand, and can add and remove cards from that hand 
    there should be an add and / remove card method here.
    """

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class player:
    """
    Player class:
    takes in a name and an instance  of a Hand class object.
    The Player can then play cards and check if they still have cards. 
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                # war_cards.append(self.hand.cards.pop())
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_have_cards(self):
        """
        return true if player still has cards left.  
        """
        return len(self.hand.cards) != 0


################################
########### Game Play ##########
################################
print("Welcome to War, let's begin ... ")


# create a new Deck and split it in half:
d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()


# create both players:
computer = player("Computer", Hand(half1))

name = input("Enter your name, please ... ")
user = player(name, Hand(half2))


total_rounds = 0
war_count = 0


while user.still_have_cards() and computer.still_have_cards():

    total_rounds += 1

    print("time for a new ROUND! ... ")
    print("here are the current standings")
    print(user.name + "has the count: " + str(len(user.hand.cards)))
    print(computer.name + " has the count: " + str(len(computer.hand.cards)))
    print("play a card")
    print("\n")

    table_cards = []

    computer_card = computer.play_card()
    user_card = user.play_card()

    table_cards.append(computer_card)
    table_cards.append(user_card)

    if computer_card[1] == user_card[1]:
        war_count += 1
        print("WAR !!!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(computer.remove_war_cards())

        if RANKS.index(computer_card[1]) < RANKS.index(user_card[1]):
            user.hand.add(table_cards)
        elif RANKS.index(computer_card[1]) > RANKS.index(user_card[1]):
            computer.hand.add(table_cards)
        else:
            if RANKS.index(computer_card[1]) < RANKS.index(user_card[1]):
                user.hand.add(table_cards)
            elif RANKS.index(computer_card[1]) > RANKS.index(user_card[1]):
                computer.hand.add(table_cards)

    else:
        if RANKS.index(computer_card[1]) < RANKS.index(user_card[1]):
            user.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)


print("Game Over ... number of rounds: " + str(total_rounds))
print("a war happend: " + str(war_count) + " times.")

if computer.still_have_cards():
    print("Computer wins ...")
else:
    print("You win ...")

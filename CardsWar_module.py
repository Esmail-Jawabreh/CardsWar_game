import random


# Define a function to create a deck of cards
def create_deck():
    # Use list comprehension to create a list of all possible card combinations
    # This assumes a standard 52-card deck with 4 suits (hearts, diamonds, clubs, spades) and 13 ranks (Ace, 2-10, Jack, Queen, King)
    ranks = [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck


# Define a function to play the game
def play_war():

    # Create the deck of cards and shuffle it
    deck = create_deck()
    random.shuffle(deck)

    # Divide the deck into two equal halves for each player
    player1_hand = deck[:len(deck)//2]
    player2_hand = deck[len(deck)//2:]

    # Initialize counters for each player's wins
    player1_wins = 0
    player2_wins = 0

    # Play the game until one player runs out of cards
    while len(player1_hand) > 0 and len(player2_hand) > 0:
        # Draw the top card from each player's hand
        player1_card = player1_hand.pop(0)
        player2_card = player2_hand.pop(0)

        # Compare the ranks of the two cards and update the win counters
        if player1_card[0] > player2_card[0]:
            player1_wins += 1
        elif player1_card[0] < player2_card[0]:
            player2_wins += 1

    # Determine the winner based on who won more rounds
    if player1_wins > player2_wins:
        print("Player 1 wins!")
    elif player1_wins < player2_wins:
        print("Player 2 wins!")
    else:
        print("It's a tie!")


# Call the play_war() function to start the game
play_war()

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:08:08 2024

@author: cherrbear
"""

import random

# Dictionary mapping card names to their values
card_values = {
    "Two of Spades": 2, "Two of Diamonds": 2, "Two of Clubs": 2, "Two of Hearts": 2,
    "Three of Spades": 3, "Three of Diamonds": 3, "Three of Clubs": 3, "Three of Hearts": 3,
    "Four of Spades": 4, "Four of Diamonds": 4, "Four of Clubs": 4, "Four of Hearts": 4,
    "Five of Spades": 5, "Five of Diamonds": 5, "Five of Clubs": 5, "Five of Hearts": 5,
    "Six of Spades": 6, "Six of Diamonds": 6, "Six of Clubs": 6, "Six of Hearts": 6,
    "Seven of Spades": 7, "Seven of Diamonds": 7, "Seven of Clubs": 7, "Seven of Hearts": 7,
    "Eight of Spades": 8, "Eight of Diamonds": 8, "Eight of Clubs": 8, "Eight of Hearts": 8,
    "Nine of Spades": 9, "Nine of Diamonds": 9, "Nine of Clubs": 9, "Nine of Hearts": 9,
    "Ten of Spades": 10, "Ten of Diamonds": 10, "Ten of Clubs": 10, "Ten of Hearts": 10,
    "Jack of Spades": 10, "Jack of Diamonds": 10, "Jack of Clubs": 10, "Jack of Hearts": 10,
    "Queen of Spades": 10, "Queen of Diamonds": 10, "Queen of Clubs": 10, "Queen of Hearts": 10,
    "King of Spades": 10, "King of Diamonds": 10, "King of Clubs": 10, "King of Hearts": 10,
    "Ace of Spades": 11, "Ace of Diamonds": 11, "Ace of Clubs": 11, "Ace of Hearts": 11
}

def draw_card(deck):
    if not deck:  # Check if the deck is empty
        return None, deck
    card_index = random.randint(0, len(deck) - 1)  # Pick a random index
    card = deck.pop(card_index)  # Remove the card from the deck
    return card, deck

# Example Usage:
deck = list(card_values.keys())  # Initialize the deck with card names
card, deck = draw_card(deck)
print("Drawn Card:", card)
print("Value of Drawn Card:", card_values[card])
print("Remaining Cards:", len(deck))


draw_card(deck)
player_card1 = card_values[card]
print(card)
draw_card(deck)
print(card)
player_card2 = card_values[card] 
print(player_card1 + player_card2)
player_hand = player_card1 + player_card2
print(player_hand)
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:34:08 2024

@author: cherrbear
"""

'''a dictionary containg a decks of cards'''
import random

single_deck={
    "Two of Spades": 2, "Three of Spades": 3,
    "Four of Spades": 4, "Five of Spades": 5,
    "Six of Spades": 6, "Seven of Spades": 7,
    "Eight of Spades": 8, "Nine of Spades": 9,
    "Ten of Spades": 10, "Jack of Spades": 10,
    "Queen of Spades": 10, "King of Spades": 10,
    "Ace of Spades": 11,
    
    "Two of Diamonds": 2, "Three of Diamonds": 3,
    "Four of Diamonds": 4, "Five of Diamonds": 5,
    "Six of Diamonds": 6, "Seven of Diamonds": 7,
    "Eight of Diamonds": 8, "Nine of Diamonds": 9,
    "Ten of Diamonds": 10, "Jack of Diamonds": 10,
    "Queen of Diamonds": 10, "King of Diamonds": 10,
    "Ace of Diamonds": 11,
    
    "Two of Clubs": 2, "Three of Clubs": 3,
    "Four of Clubs": 4, "Five of Clubs": 5,
    "Six of Clubs": 6, "Seven of Clubs": 7,
    "Eight of Clubs": 8, "Nine of Clubs": 9,
    "Ten of Clubs": 10, "Jack of Clubs": 10,
    "Queen of Clubs": 10, "King of Clubs": 10,
    "Ace of Clubs": 11,
    
    "Two of Hearts": 2, "Three of Hearts": 3,
    "Four of Hearts": 4, "Five of Hearts": 5,
    "Six of Hearts": 6, "Seven of Hearts": 7,
    "Eight of Hearts": 8, "Nine of Hearts": 9,
    "Ten of Hearts": 10, "Jack of Hearts": 10,
    "Queen of Hearts": 10, "King of Hearts": 10,
    "Ace": 11
    }

#add the suits to the dictionaries and make one list of all 52 cards 
#**make a list of the keys from the dict, randomly select 2 from the list
#**use list_name.pop(variable_with_2_keys[0]) and one with [1] for the index of the keys in the list
#**to take them from the list. add them and go on with dealing the game


print(single_deck)
random_value1 = random.choice(list(single_deck.values())) # .values gets the value of the key value pair(dict)
random_value2 = random.choice(list(single_deck.values())) # .keys gets the key from the key value pair (dict)
print(random_value1, random_value2)
card1 = random_value1
card2 = random_value2  
print(card1, card2)

hand = print(f'you have {card1 + card2}')




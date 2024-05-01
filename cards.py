# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:00:54 2024.

@author: CherrBear

This module handles card operations.

"""
import random


deck_1 = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
]

player_hand = []  # creates empty player list to store cards
dealer_hand = []

discard = []  # Intialize an empty discard rack.

def deal_hand(hand):
    """
    Start the hand giving 2 cards.

    Args:
        a (list): The empty player or dealer_hand list.

    Returns:
        list: List with 2 random values from deck_1.
    """
    if len(hand) == 0:
        for _ in range(2):
            card_index = random.randrange(len(deck_1))
            hand.append(deck_1.pop(card_index))
    return hand


def hit(player_or_dealer):
    """
    Draw a random 'card' from deck_1 and adds it to player/dealer list.

    Args:
        a (list): player / dealer_hand list.

    Returns:
        list: Value from deck_1 appended to player/dealer list.
    """
    if deck_1:  # checks for items in list, 1 or more items it executes
        card_index = random.randrange(len(deck_1))
        player_or_dealer.append(deck_1.pop(card_index))
    else:
        print('Time to shuffle!\n\n')
        
        #  SHUFFLE FUNCTION HERE
    
    return player_or_dealer

    
def discards(player, dealer):
    """
    Collect player and dealer cards after the hand.
    
    Args:
        a (list): Player or dealer list values after hand.
        
    Returns:
        None.
    """
    if len(deck_1) <= 15:
        global discard
       
        discard.extend(deck_1)
        discard.extend(player_hand)
        discard.extend(dealer_hand)
        shuffle()
        print(f'SHUFFLE DECK: {deck_1} \n\n DISCARD: {discard}')
    else:
        discard.extend(player_hand)
        player_hand.clear()
        print(player_hand)
        discard.extend(dealer_hand)
        dealer_hand.clear()
        print(dealer_hand)
        
        print(f'\n\n\nDeck 1: {deck_1} \n\n{len(deck_1)}\n\n\n')
        
    print(discard)
    return discard
    
    
def shuffle():
    """
    Return cards to deck_1 when theres 15 or less.
    
    Args:
        None.
        
    Returns:
        None.
    """
    deck_1.extend(discard)
    discard.clear()
    print(f'SHUFFLE DECK: {deck_1} \n\n DISCARD: {discard}')

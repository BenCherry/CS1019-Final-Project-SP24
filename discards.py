# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:55:44 2024

@author: cherrbear

Migrated to cards module

"""

from cards import deck_1, discard
from cards import player_hand, dealer_hand



def discards(used_cards):
    """
    Collect player and dealer cards after the hand.
    
    Args:
        a (list): Player or dealer list values after hand.
        
    Returns:
        None.
    """
    for card in range(len(used_cards)):
        print(used_cards)
        used_card = used_cards.pop()
        discard.append(used_card)
        print(used_cards)
        print(f'Discards: {discard}, Deck_1: {deck_1, len(deck_1)}')
        
def shuffle():
    """
    Return cards to deck_1 when theres 15 or less.
    
    Args:
        None.
        
    Returns:
        None.
    """
    
    if len(deck_1) <= 15:
        print('Sorry, we have to kill the hand.(This hand is over)')
        discards(player_hand)
        discards(dealer_hand)
        for card in discard:
            shuffling = discard.pop(card)
            deck_1.append(shuffling)
        print('New shoe, let\'s play!')
    
    #else
            
    
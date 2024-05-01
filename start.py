# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:36:47 2024.

@author: cherrbear
"""
from cards import player_hand, dealer_hand, deck_1
from cards import deal_hand, discards, shuffle, discard

from gameplay import player_turn, dealer_turn

from results import winning_hand


def start_game():
    """
    NEEDS DOCSTRING
    """
    print(f' discards: {discard}')
    deal_hand(player_hand)
    print(f'You have: {sum(player_hand)}\n\n')
    
    deal_hand(dealer_hand)
    print(f'Dealer shows: {dealer_hand[0]}\n\n')  # Show dealer first card only
    
    player_turn()
    dealer_turn()
    
    winning_hand(player_hand, dealer_hand)
    
    discards(player_hand, dealer_hand)
    #discards(dealer_hand)

    
    # if len(deck_1) <= 15:
    #     shuffle()

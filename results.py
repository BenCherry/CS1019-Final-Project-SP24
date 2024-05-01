# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:17:11 2024

@author: CherrBear

THIS MODULE COMPARES AND DETERMINES THE WINNING HAND

"""
from gameplay import dealer_count
from gameplay import player_count
from cards import discards

def winning_hand(player_hand, dealer_hand):
    """
    Compare the hands and returns the result (win / lose/ push).

    Args:
        a (list): The player_hand list.
        b (list): The dealer_hand list.

    Returns:
        str: Prints the winner.
    """
    if player_count() is True:
        print(f'You bust with: {sum(player_hand)}\n\n')

    elif dealer_count() is True:
        print(f'Dealer busts with: {sum(dealer_hand)} '
              f'Player wins with: {sum(player_hand)}\n\n')

    elif sum(dealer_hand) == sum(player_hand):
        print("A push is a win\n\n")

    elif sum(dealer_hand) < sum(player_hand):
        print(f'Dealer has a {sum(dealer_hand)}, '
              f' you win with a {sum(player_hand)}\n\n')

    elif sum(dealer_hand) > sum(player_hand):
        print(f'Dealer wins with a {sum(dealer_hand)}\n\n')

    

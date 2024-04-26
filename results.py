# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:17:11 2024

@author: CherrBear

THIS MODULE COMPARES AND DETERMINES THE WINNING HAND

"""


def winning_hand(player_hand, dealer_hand):
    """
    Compare the hands and returns the result (win / lose/ push).

    Args:
        a (none): None.

    Returns:
        str: Prints the winner.
    """    
    if player_count() is True:
        print(f'You bust with: {sum(player_hand)}\n')
    
    elif dealer_count() is True:
        print(f'Dealer busts with: {sum(dealer_hand)} '
              f'Player wins with: {sum(player_hand)}\n')
    
    elif sum(dealer_hand) == sum(player_hand):
        print("A push is a win\n") 

    elif sum(dealer_hand) < sum(player_hand):
        print(f'Dealer has a {sum(dealer_hand)}, '
              f' you win with a {sum(player_hand)}\n')
    
    elif sum(dealer_hand) > sum(player_hand):
        print(f'Dealer wins with a {sum(dealer_hand)}\n')
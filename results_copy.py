# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:33:33 2024

@author: cherrbear
"""

from gameplay_copy import dealer_count
from gameplay_copy import player_count


def winning_hand(player_totals, dealer_totals):
    """
    Compare the hands and returns the result (win/ lose/ push).

    Args:
        a (list): The player_hand list.
        b (list): The dealer_hand list.

    Returns:
        str: Prints the winner.
    """
    if player_count(player_totals) is True:
        print(f'You bust with: {player_totals}\n')

    elif dealer_count(dealer_totals) is True:
        print(f'Dealer busts with: {dealer_totals} '
              f'Player wins with: {player_totals}\n')

    elif dealer_totals == player_totals:
        print("A push is a win\n")

    elif dealer_totals < player_totals:
        print(f'Dealer has a {dealer_totals}, '
              f' you win with a {player_totals}\n')

    elif dealer_totals > player_totals:
        print(f'Dealer wins with a {dealer_totals}\n')

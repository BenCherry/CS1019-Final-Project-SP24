# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:17:11 2024

@author: CherrBear

This module compares the final total of the hands and outputs the result.

"""

from gameplay import player_count, dealer_count


def winning_hand(player_totals, dealer_totals):
    """
    Compare the hands and returns the result (win/ lose/ push).

    Args:
        player_totals (int): Final calculated player score.

        dealer_totals (int): Final calculated dealer score.

    Returns:
        None.
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

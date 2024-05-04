# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:32:17 2024

@author: cherrbear
"""

from cards_copy import player_hand, dealer_hand
from cards_copy import deal_hand, discards, discard, deck_1

from gameplay_copy import player_turn, dealer_turn

from results_copy import winning_hand


def start_game():
    """
    Call functions that run the game.

    Args:
        None.

    Returns:
        None.
    """
    player_total = deal_hand(player_hand)

    print(f'You have: {player_total}\n')

    dealer_total = deal_hand(dealer_hand)

    print(f'Dealer shows: {dealer_hand[0]}\n')  # Show dealer first card only

    player_total = player_turn(player_total)

    dealer_total = dealer_turn(dealer_total, player_total)

    winning_hand(player_total, dealer_total)
    print(f'Players Cards: {player_hand}\n\nDealers Cards: {dealer_hand}\n\n')

    discards(player_hand, dealer_hand)

    print(f'Cards Remaining: {len(deck_1)} \n\n{deck_1} '
          f'\n\nCards Used: {len(discard)} \n\n{discard}')

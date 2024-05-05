# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:36:47 2024.

@author: cherrbear

This module calls the base functions that run the game.

The print statement at the bottom can be commented out to
make the console more readable during execution, or left
to keep track of the cards in each hand, the deck, and the discards.

"""

from cards import player_hand, dealer_hand
from cards import deal_hand, discards
from cards import deck_1, discard  # Cards remaining and discards

from gameplay import player_turn, dealer_turn

from results import winning_hand


def start_game():
    """
    Call functions that run the game.

    Args:
        None.

    Returns:
        None.
    """
    player_total = deal_hand(player_hand)
    print(f'You have {player_total}\n')

    dealer_total = deal_hand(dealer_hand)
    print(f'Dealer shows {dealer_hand[0]}\n')  # Show dealer first card only

    player_total = player_turn(player_total)

    dealer_total = dealer_turn(dealer_total, player_total)

    winning_hand(player_total, dealer_total)
    print(f'Players Cards {player_hand}\n\nDealers Cards {dealer_hand}\n\n')

    discards(player_hand, dealer_hand)

    print(f'Cards Remaining: {len(deck_1)} \n\n{deck_1} '   # Cards remaining
          f'\n\nCards Used: {len(discard)} \n\n{discard}')  # Discards

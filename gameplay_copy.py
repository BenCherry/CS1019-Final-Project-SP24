# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:31:25 2024

@author: cherrbear
"""

from cards_copy import hit
from cards_copy import player_hand, dealer_hand


def player_turn(players_total):
    """
    Determine if the player draws more cards or stays.

    Args:
        a (none) None.

    Return:
        list: Finished player_hand list.
    """
    while players_total < 21:
        hand_signal = input('Press "H" to hit, or any key to stay: \n\n')
        if hand_signal.upper() == 'H':
            players_total = hit(player_hand)
            if player_count(players_total) is True:
                break
            print(f'You hit for a total of: {players_total}\n\n')
        elif hand_signal != 'H':
            print(f'You stay with {players_total}\n\n')
            break
    return players_total


def player_count(players_total):
    """
    Set bust to False, or True if player_hand > 21.

    Args:
        a (list): player_hand list with elements.

    Returns:
        bool: bust as True or False.
    """
    player_bust = False
    if players_total > 21:
        player_bust = True
    return player_bust


def dealer_turn(dealers_total, players_total):
    """
    Determine if the dealer draws more cards or stays.

    Args:
        a (none) None.

    Return:
        list: Finished dealer_hand list.
    """
    while dealers_total < 17:
        if players_total == 21 and len(player_hand) == 2:  # Skip dealer if player has 21
            break
        if player_count(players_total) is True:  # Skip dealer draw if player_hand > 21
            break
        dealers_total = hit(dealer_hand)
        print(f'Dealer hits for a total of: {dealers_total}\n\n')
        if dealer_count(dealers_total) is True:
            break
    return dealers_total


def dealer_count(dealers_total):
    """
    Set bust to False, or True if dealer_hand > 21.

    Args:
        a (list): dealer_hand list with elements.

    Returns:
        bool: bust as True or False.
    """
    dealer_bust = False
    if dealers_total > 21:
        dealer_bust = True
    return dealer_bust

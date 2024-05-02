# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:05:44 2024.

@author: CherrBear

THIS MODULE DEALS WITH THE PLAYER AND DEALER TURNS.

FUNCS PLAYER/DEALER_TURN DEAL WITH GETTING CARDS

FUNCS PLAYER/DEALER_COUNT DETERMINE IF THE HAND BUSTS

"""

from cards import hit
from cards import player_hand, dealer_hand


def player_turn():
    """
    Determine if the player draws more cards or stays.

    Args:
        a (none) None.

    Return:
        list: Finished player_hand list.
    """
    while sum(player_hand) < 21:
        hand_signal = input('Press "H" to hit, or any key to stay: \n\n')
        if hand_signal.upper() == 'H':
            hit(player_hand)
            if player_count() is True:
                break
            print(f'You hit for a total of: {sum(player_hand)}\n\n')
        elif hand_signal != 'H':
            print(f'You stay with {sum(player_hand)}\n\n')
            break


def player_count():
    """
    Set bust to False, or True if player_hand > 21.

    Args:
        a (list): player_hand list with elements.

    Returns:
        bool: bust as True or False.
    """
    player_bust = False
    if sum(player_hand) > 21:
        player_bust = True
    return player_bust


def dealer_turn():
    """
    Determine if the dealer draws more cards or stays.

    Args:
        a (none) None.

    Return:
        list: Finished dealer_hand list.
    """
    while sum(dealer_hand) < 17:
        if player_count() is True:  # Skip dealer draw if player_hand > 21
            break
        hit(dealer_hand)
        print(f'Dealer hits for a total of: {sum(dealer_hand)}\n\n')
        if dealer_count() is True:
            break


def dealer_count():
    """
    Set bust to False, or True if dealer_hand > 21.

    Args:
        a (list): dealer_hand list with elements.

    Returns:
        bool: bust as True or False.
    """
    dealer_bust = False
    if sum(dealer_hand) > 21:
        dealer_bust = True
    return dealer_bust

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
    NEEDS DOCSTRING
    """
    while sum(player_hand) < 21:
        hand_signal = input('Press "H" to hit, or any key to stay: \n')
        if hand_signal == 'h':
            hit(player_hand)
            if player_count() is True:
                break
            print(f'You hit for a total of: {sum(player_hand)}\n')
        elif hand_signal != 'h':
            print(f'You stay with {sum(player_hand)}\n')
            break


def player_count():
    """
    NEEDS DOCSTRING
    """
    bust = False
    if sum(player_hand) > 21:
        bust = True
    return bust


def dealer_turn():
    """
    Determine if the dealer draws more cards or stays.

    Args:
        a (none) None.

    Return:
        list: Finished dealer_hand list.
    """
    while sum(dealer_hand) < 17:
        if player_count is True:  # Skip dealer draw if player_hand > 21
            break
        hit(dealer_hand)
        print(f'Dealer hits for a total of: {sum(dealer_hand)}\n')
        if dealer_count() is True:
            break


def dealer_count():
    """
    NEEDS DOCSTRING
    """
    bust = False
    if sum(dealer_hand) > 21:
        bust = True
    return bust

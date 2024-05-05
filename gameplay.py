# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:05:44 2024.

@author: CherrBear

This module handles gameplay related to player and dealer decisions.

"""

from cards import hit
from cards import player_hand, dealer_hand


def player_turn(players_total):
    """
    Determine if the player draws more cards, busts, or stays.

    Args:
        players_total (int): Current total of the players hand.

    Return:
        int: Final player total.
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
        players_total (int): Current total of the players hand.

    Returns:
        bool: True if player busts, False otherwise..
    """
    player_bust = False
    if players_total > 21:
        player_bust = True
    return player_bust


def dealer_turn(dealers_total, players_total):
    """
    Determine if the dealer draws more cards or stays.

    Args:
        dealers_total (int): Current total of the dealers hand.

        players_total (int): Current total of the players hand.

    Return:
        int: Final dealer total.
    """
    while dealers_total < 17:
        if players_total == 21 and len(player_hand) == 2:
            break
        if player_count(players_total) is True:
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
        dealers_total (int): Current total of the dealers hand.

    Returns:
        bool: True if dealer busts, false otherwise.
    """
    dealer_bust = False
    if dealers_total > 21:
        dealer_bust = True
    return dealer_bust

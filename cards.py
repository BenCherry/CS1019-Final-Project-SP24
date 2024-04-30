# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:00:54 2024.

@author: CherrBear

Thia module handles card operations.

"""
import random


deck_1 = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
]

player_hand = []  # creates empty player list to store cards
dealer_hand = []


def deal_hand(hand):
    """
    Start the hand giving 2 cards.

    Args:
        a (list): The empty player or dealer_hand list.

    Returns:
        list: List with 2 random values from deck_1.
    """
    if len(hand) == 0:
        for _ in range(2):
            card_index = random.randrange(len(deck_1))
            hand.append(deck_1.pop(card_index))
    return hand


def hit(player_or_dealer):
    """
    Draw a random 'card' from deck_1 and adds it to player/dealer list.

    Args:
        a (list): player / dealer_hand list.

    Returns:
        list: Value from deck_1 appended to player/dealer list.
    """
    if deck_1:  # checks for items in list, 1 or more items it executes
        card_index = random.randrange(len(deck_1))
        player_or_dealer.append(deck_1.pop(card_index))
    else:
        print('Time to shuffle!\n')
    return player_or_dealer

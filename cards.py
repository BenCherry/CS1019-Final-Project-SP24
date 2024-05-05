# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:00:54 2024.

@author: CherrBear

This module handles list initialization and card operations.

"""


import random
deck_1 = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
]

player_hand = []  # Creates empty player list to store cards.
dealer_hand = []  # Creates empty dealer list to store cards.

discard = []  # Intialize an empty discard rack.


def deal_hand(hand):
    """
    Start the hand giving 2 cards.

    Args:
        hand (list): The empty player or dealer_hand list.

    Returns:
        int: Local variable with integer value of the hand.

    """
    if len(hand) == 0:
        for _ in range(2):
            card_index = random.randrange(len(deck_1))
            hand.append(deck_1.pop(card_index))
    hand_total = aces(hand)
    return hand_total


def aces(hand):
    """
    Change 'Ace' value based on hand total and / or multiple 'Aces'

    Args:
        hand (list): Player or dealer_hand list.

    Returns:
        int: Local variable with the updated hand value.
    """
    total = sum(hand)
    ace = hand.count(11)

    while total > 21 and ace:
        total -= 10
        ace -= 1
    return total


def hit(hand):
    """
    Draw a card and assign a new hand value.

    Args:
        hand (list): Player or dealer_hand list.

    Returns:
        int: Local variable with the updated hand value.
    """
    card_index = random.randrange(len(deck_1))
    hand.append(deck_1.pop(card_index))

    hand_total = aces(hand)

    return hand_total


def discards(players_hand, dealers_hand):
    """
    Collect cards after the hand and shuffle if needed. 

    Args:
        players_hand (list): Player list with elements.

        dealers_hand (list): Dealer list with elements.

    Returns:
        None.
    """
    if len(deck_1) <= 15:
        discard.extend(deck_1)

        discard.extend(players_hand)
        players_hand.clear()

        discard.extend(dealers_hand)
        dealers_hand.clear()

        shuffle()

    else:
        discard.extend(players_hand)
        players_hand.clear()

        discard.extend(dealers_hand)
        dealers_hand.clear()


def shuffle():
    """
    Clear deck_1, add 52 cards from discard to it, clear discard.

    Args:
        None.

    Returns:
        None.
    """
    deck_1.clear()
    deck_1.extend(discard)
    discard.clear()

    print(f'\nSHUFFLE DECK: {len(deck_1)} DISCARD: {len(discard)}')

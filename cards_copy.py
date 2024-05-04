# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:26:52 2024

@author: cherrbear
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:00:54 2024.

@author: CherrBear

This module handles card operations.

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
        a (list): The empty player or dealer_hand list.
        b (var):  Player / dealer_total
    Returns:
        list: List with 2 random values from deck_1.
    """
    if len(hand) == 0:
        for _ in range(2):
            card_index = random.randrange(len(deck_1))
            hand.append(deck_1.pop(card_index))
    hand_total = aces(hand)
    return hand_total


def aces(hand):
    """


    Args:
        a (list): Player or dealer list.

    Returns:
        var: Variable with the new multi ace value.
    """
    total = sum(hand)
    ace = hand.count(11)  #

    while total > 21 and ace:
        total -= 10
        ace -= 1
    return total


"""
Combined with deal_hand 
"""


def hit(hand):
    """
    Draw a random 'card' from deck_1 and adds it to player/dealer list.

    Args:
        a (list): player / dealer_hand list.

    Returns:
        list: Value from deck_1 appended to player/dealer list.
    """
    card_index = random.randrange(len(deck_1))
    hand.append(deck_1.pop(card_index))

    hand_total = aces(hand)

    return hand_total


def discards(players_hand, dealers_hand):
    """
    Collect player and dealer cards after the hand.

    Args:
        a (list): Player list with elements.
        b (list): Dealer list with elements.
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
    Clear remaining deck_1 elements, then add 52 from discard.

    Args:
        None.

    Returns:
        None.
    """
    deck_1.clear()
    deck_1.extend(discard)
    discard.clear()

    print(f'\nSHUFFLE DECK: {len(deck_1)} DISCARD: {len(discard)}')

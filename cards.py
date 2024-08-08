# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:00:54 2024.

@author: CherrBear

This module handles list initialization and card operations.

aces function - In blackjack, an Ace can be worth 11 or 1 depending on
the hand total. A single ace in a hand is worth 11, until the hand total
goes over 21, at which point it becomes a 1.

example_hand: (deal) Ace + 5 == 16 (draw) + 10 == 26 (adjust) == 16 (1 + 5 + 10)

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
        int: The total value of the hand.

    """
    if len(hand) == 0:
        for _ in range(2):
            card_index = random.randrange(len(deck_1))
            hand.append(deck_1.pop(card_index))
    hand_total = aces(hand)
    return hand_total


def aces(hand):
    """
    Change 'Ace' value to 1 or 11 based on hand total.

    Args:
        hand (list): Player or dealer_hand list.

    Returns:
        int: The adjusted total value of the hand.
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
        int: The adjusted total value of the hand.
    """
    card_index = random.randrange(len(deck_1))
    hand.append(deck_1.pop(card_index))

    hand_total = aces(hand)

    return hand_total


def discards(players_hand, dealers_hand):
    """
    Collect cards after the hand and shuffle if needed. 

    Args:
        players_hand (list): Player list.

        dealers_hand (list): Dealer list.

    Returns:
        None.
    """
    if len(deck_1) <= 15:  # About how many cards left before shuffling a real 1 deck game.
        discard.extend(deck_1)  # Add remaining cards in the deck to discard.

        discard.extend(players_hand)  # Add player cards to discard.
        players_hand.clear()

        discard.extend(dealers_hand)  # Add dealer cards to discard.
        dealers_hand.clear()

        shuffle()

    else:
        discard.extend(players_hand)  # Discard player and dealer cards only if not shuffling.
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

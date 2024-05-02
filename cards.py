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

player_hand = []  # creates empty player list to store cards
dealer_hand = []

discard = []  # Intialize an empty discard rack.


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
    if deck_1:
        card_index = random.randrange(len(deck_1))
        player_or_dealer.append(deck_1.pop(card_index))

    return player_or_dealer


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
        print('discard.extend(deck_1)  if')
        
        discard.extend(players_hand)
        players_hand.clear()
        print('discard.extend(players_hand) if')
        
        discard.extend(dealers_hand)
        dealers_hand.clear()
        print('discard.extend(dealers_hand)  if')
        
        shuffle()
        print('shuffle  if')

    else:
        discard.extend(players_hand)
        print('discard.extend(players_hand)  else')
        
        players_hand.clear()
        print('players_hand.clear()  else')
        
        discard.extend(dealers_hand)
        print('discard.extend(dealers_hand)  else')
        
        dealers_hand.clear()
        print('dealers_hand.clear()  else')

        print(f'\nDeck 1:Cards Remaining: {len(deck_1)}')
        print(f'Discard list cards: {len(discard)}\n')


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

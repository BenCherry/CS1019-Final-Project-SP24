# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:43:12 2024

@author: CherrBear

SPRING 2024 CS1019 TERM PROJECT

MAIN FILE

"""
from cards import deal_hand
from gameplay import player_turn, dealer_turn
from results import winning_hand


def main():
    """
    NEEDS DOCSTRING
    """
    deal_hand(player_hand)
    print(f'You have: {sum(player_hand)}\n')
    deal_hand(dealer_hand)
    print(f'Dealer shows: {dealer_hand[0]}\n')  # Show dealer first card only
    player_turn()
    dealer_turn()
    winning_hand()

if __name__ == '__main__':
    main()
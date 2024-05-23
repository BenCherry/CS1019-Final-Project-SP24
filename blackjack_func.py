# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:04:22 2024

@author: cherrbear
"""
# from cards import player_hand, dealer_hand
#player_hand = 21
player_hand = [11, 10]  # TEST values
dealer_hand = [10, 11]  # TEST values
black_jack = (10, 11)


def dealer_10_up(player_hand, dealer_hand):
    """
    """
    if dealer_hand[0] == 10 and \
            dealer_hand == black_jack:

        if player_hand == 21:
            #  Need to push the hand
            print('(Need to add a push function here (BJ Function))')
        elif player_hand != 21:
            #  Player loses
            print('(Player loses to dealer BJ here (BJ Function)')

    elif dealer_hand[0] == 10 and \
            dealer_hand != black_jack:

        if sum(player_hand) == 21:
            #  Pay the player here
            print('Player wins with a BJ here (BJ Function)')
        else:
            #  Need to continue the hand here
            print('The hand continues here (BJ Function)')


dealer_10_up(player_hand, dealer_hand)


# def blackjack(players_hand, dealers_hand):
#     """
#     Checks for blackjacks


#     """
#     black_jack = (10, 11)

#     if player_hand == 21 or \
#             dealer_hand[0] in black_jack:

#         if dealer_hand[0] == 10:


#         if dealer_hand[0] == 10 and \
#                 dealer_hand == black_jack:
#             print(f'{dealer_hand}, Dealer has BlackJack, we push')
#             # Need to push if player has BJ too

#         elif dealer_hand[0] == 10 and \
#                 dealer_hand != black_jack:
#             # Pay the player
#             print('You win with a Blackjack!')

#         elif dealer_hand[0] == 11:
#             # Offer even money
#             print('Would you like even money?')

#         else:
#             print('You win with a BJ!')

#     elif sum(player_hand) != 21:
#         if dealer_hand[0] == 10 and \
#                 dealer_hand == black_jack:
#             print(f'{dealer_hand}, Dealer wins with a BlackJack')

#         elif dealer_hand[0] == 10 and \
#                 dealer_hand != black_jack:
#             print('No BJ, lets move on')

#         elif dealer_hand[0] == 11:
#             # Need to offer insurance
#             print('Would you like insurance?')


# # while any(card in hand for card in black_jack):
# if player_hand == 21 or \
#         dealer_hand[0] in black_jack:

#     if sum(player_hand) == 21:

#         if dealer_hand[0] == 10 and \
#                 dealer_hand == black_jack:
#             print(f'{dealer_hand}, Dealer has BlackJack, we push')
#             # Need to push if player has BJ too

#         elif dealer_hand[0] == 10 and \
#                 dealer_hand != black_jack:
#             # Pay the player
#             print('You win with a Blackjack!')

#         elif dealer_hand[0] == 11:
#             # Offer even money
#             print('Would you like even money?')

#         else:
#             print('You win with a BJ!')

#     elif sum(player_hand) != 21:
#         if dealer_hand[0] == 10 and \
#                 dealer_hand == black_jack:
#             print(f'{dealer_hand}, Dealer wins with a BlackJack')

#         elif dealer_hand[0] == 10 and \
#                 dealer_hand != black_jack:
#             print('No BJ, lets move on')

#         elif dealer_hand[0] == 11:
#             # Need to offer insurance
#             print('Would you like insurance?')


# blackjack(player_hand, dealer_hand)

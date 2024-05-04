# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:32:57 2024

@author: cherrbear
"""


from start_copy import start_game


def main():
    """
    Main function that runs the program.

    Returns
    -------
    None.

    """

    user_start = ' '

    while user_start not in ['P', 'Q']:
        user_start = input('\nPress P to play, or Q to quit: \n')
        if user_start.upper() == 'P':
            print('\nLet\'s play!\n')
            start_game()
        elif user_start.upper() == 'Q':
            print('Exiting\n')
            break

        else:
            print('Enter a valid choice.\n')


if __name__ == '__main__':
    main()

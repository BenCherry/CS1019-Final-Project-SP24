# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:08:32 2024

@author: cherrbear
"""

def buy_in():
    while True:
        amount = input('Buying in? $')
        if amount.isdigit():# .isdigit() returns True if all characters in the
            amount = int(amount)#converts string to integer # string are digits
            if amount > 0:
                break# end function for valid amount
            else:
                print('Amount must be greater than 0.')#user enters a neg num
        else:
            print(amount)
            print('Must be a number: $')#user enters a letter, symbol, etc...
    print(type(amount))      
    return amount#returns the value of amount 

buy_in()

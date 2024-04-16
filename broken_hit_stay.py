# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:11:48 2024

@author: cherrbear
"""

def hit_or_stay(hit_or_stay):
    hit_or_stay == 'h' or 's'
    input('Press "H" to hit, or "S" to stay')
    while hit_or_stay != 'h' or 's':
        input('Please press "H" to hit \nor \n"S" to stay')

        
print(f'hit or stay {hit_or_stay(hit_or_stay)}')


hit = input('H to hit S to stay')
hit_hand = 'h'
stay_hand = 's'

while hit != (hit_hand) or (stay_hand):    #FIXME infinite loop
    hit_hand == 'h'
    stay_hand == 's'
    hit = input('Press "H" to hit, or "S" to stay. ')
    
if hit == 'h':
    print('hite')
elif hit == 's':
    print('stay')
else:
    print('WTF?')
print(hit)
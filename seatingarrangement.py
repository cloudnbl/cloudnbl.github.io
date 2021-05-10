# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:35:28 2021
#seatingarrangement challenge where two people should be sitting next to each other always
@author: blapa
"""
from itertools import combinations

def is_pair_valid(pair, occupied_list):
    # check occupied
    x, y = min(pair), max(pair)
    if x in occupied_list or y in occupied_list:
        return False
    # check neighbours
    diff = y - x
    return diff in (2, 1, -2) if x % 2 == 1 else diff in (2, -1, -2)
def seatingarrangement (arr): 
    #int array
    arry = arr.split(',')
    larr = [int(x) for x in arry]
    #total items and occupied list
    total = (larr[0])
    occ = larr[1:]  
         
    totals = [x+1 for x in range(0,total)]
    print("total seats: ",totals) 
    
    #filtering if each comb only includes unoccupied neighbors
    valid = list(filter(lambda x: is_pair_valid(x, occ),combinations(totals, r=2)))
    return valid
print(seatingarrangement(input('enter your list:: ' )))

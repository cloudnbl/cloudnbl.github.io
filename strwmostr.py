# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:35:28 2021
#input a string and find the word with most repeating letters and print the word 
@author: blapa
"""
import collections
from collections import Counter
def counttheletters(in_str):
    # Create list of word tuples: (word, max_letter, max_count)
    #counters = [ (word, *max(Counter(word).items(), key=lambda item: item[1])) for word in in_str.split() ]
 #    max_word, max_letter, max_count = len(counters, key=lambda item: item[2])
  #  return max_word   
         
    max_repeat_count = 0
    l_ofwords=in_str.split(' ')    
    for word in l_ofwords:
        occurances = {}
        for c in word:
            if c not in occurances:
                occurances[c] = 1
            else:
                occurances[c] += 1
            if occurances[c]> max_repeat_count:
                max_repeat_count = occurances[c]
                #most_repeated_char = c
                result=word
    return result
#print(counttheletters(input('enter your input:: ' )))
def longests(string):
    long = {}  
   # lists = sorted(string.split(),key=len)  return lists[-1]
    for word in string.split(): 
       long[word]  = len(word)
   # lkeys = list(long.keys())
   # lvals = list(long.values())    
    #return lkeys[lvals.index(max(lvals))]
    for key,val in long.items():
        if val == max(long.values()):
            return key
#print(longests(input('enter your string::')))
def textpro():
    in_notes=''
    results=[]
    def checq(inp):
        q_list = ('how','who','where','Did','why','whom', 'what') 
        
        if (inp.startswith (q_list)):
             return "{}?".format(inp)
        else:
             return "{}.".format(inp)
    
    inp = input('say something::')  
     
    while(inp): 
        if inp == r"\end":
            print(in_notes)
            break
        else:
            inp = checq(inp)
            in_notes += inp.capitalize()  
            results.append(inp.capitalize())
            inp = input('say something::')
    print(' '.join(results))     
textpro()
        
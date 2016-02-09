# -*- coding: utf-8 -*-

def golf(coins):
    import operator as o
    import itertools as d
    a = coins
    stuff = [[i] for i in a]
    print stuff
    for list1 in d.product(*stuff)):
        print list1
    #f = [c for i in range(len(coins)) for c in d.combinations(coins, i+1)]
    #second = list(set([sum(i) for i in f]))
    #return f


    


'''
golf([9, 2, 2, 1]) == 6
golf([1, 1, 1, 1]) == 5
golf([1, 2, 3, 4, 5]) == 16
'''

print golf([9, 2, 2, 1])
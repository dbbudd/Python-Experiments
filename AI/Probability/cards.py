#!/usr/bin/env python

import random
import operator
import itertools
from scipy.stats import hypergeom
import numpy as np

cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
print(cards)

random.shuffle(cards)

print(cards)



def card_add(sum, x):
    if x < 10:
        sum += x
    else:
        sum += 10
    return sum


player = []
house = []

print(len(cards))

player.append(cards.pop())
house.append(cards.pop())

print("House = " + str(sum(house)) + "..." + str(house))
print("Player = " + str(sum(player)) + "..." + str(player))

player.append(cards.pop())
house.append(cards.pop())

print("House = " + str(sum(house)) + "..." + str(house))
print("Player = " + str(sum(player)) + "..." + str(player))

count = 0
for item in cards:
    if item <= (21-sum(player)):
        count +=1

#print("count:" + str(count))
length = len(cards)
#print("length:" + str(length))

average = 100.0 * count / length
print(str(average) + "%")

if average > 50.0:
    player.append(cards.pop())
    house.append(cards.pop())
else:
    house.append(cards.pop())


print("House = " + str(sum(house)) + "..." + str(house))
print("Player = " + str(sum(player)) + "..." + str(player))



  
print("""
      .
      .
      .
      .
      """)



'''
combos2 = []


for i in itertools.permutations(cards, 2):
    if i[0] + i[1] < 21:
        combos2.append(i)
print(combos2)


total = []
for i in itertools.permutations(cards, 2):
    total.append(i)

totalLen = len(total)

for pair in itertools.product(player, cards):
    for a,b in itertools.permutations(pair, 2):
        if a + b < 21:
            combos2.append(pair)

comboLen = len(combos2)
print(comboLen)
print(totalLen)

[M, n, N] = [52, 4, 5]

rv = hypergeom(M, n, N)
x= np.arange(0, n+1)
pmf_cards = rv.pmf(x)

print(pmf_cards)

print("")

'''







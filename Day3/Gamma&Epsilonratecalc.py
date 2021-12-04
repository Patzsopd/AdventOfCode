# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:45:57 2021

@author: Pat Zazzaro
"""

from collections import Counter
from copy import deepcopy
import math

# Part 1 (Calculating gamma power)

#Getting Data from file
BinData = open("BinData.txt","r")
content = BinData.readlines()
my_list = [line.rstrip('\n') for line in content]
BinData.close()

counters = [Counter() for _ in range(12)]

for i in range(12):
    for line in my_list:
        counters[i].update((line[~i],))

#print(counters)

gamma = 0
epsilon = 0

for j in range(12):
    higher = counters[j].most_common()
    gamma |= int(higher[0][0]) << j
    epsilon |= int(higher[1][0]) << j
    
ans = (gamma * epsilon)

print(f"Answer to part 1: {ans}")
print()

# part 2 (Calculating Oxy & Life support)

def Bitfind(mode, rev=False) -> str:
    if mode == ">":
        return '1' if not rev else '0'
    else:
        return '0' if not rev else '1'
    
def comm(target, i, mode) -> str:
    th = math.floor(sum(1 for _ in target) / 2) + 1
    z , o = 0,0
    
    for x in range(0,len(target)):
        if target[x][i] == '0':
            z += 1
        else:
            o += 1
    
        if z >= th:
            return Bitfind(mode, True)
        if o >= th:
            return Bitfind(mode)
    return Bitfind(mode)

operator = ['>', '<']
op_blank = []
bitlength = len(my_list[0])
#print(bitlength)

for a in operator:
    copy = deepcopy(my_list)
    
    for b in range(0, bitlength):
        act = comm(copy, b, a)
        copy = [n for n in copy if n[b] == act]
        
        if len(copy) == 1:
            break
        
    op_blank.append(copy[0])
    

print(op_blank)
oxygen = int(op_blank[0], 2)
co2scrub = int(op_blank[1], 2)
print(oxygen,co2scrub)
print()

ans2 = oxygen*co2scrub
print(f"Answer to part 2: {ans2}")

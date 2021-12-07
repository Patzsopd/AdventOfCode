# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 22:02:18 2021

@author: Pat Zazzaro
"""

import math
import numpy as np



# Part 1
with open('Day6Input.txt') as f:
    Fishes = f.read()

#Fishes.split(",")
Fishes = [int(x.strip()) for x in Fishes.split(",")]

day = 0
dayf = 256

#Initalstate = [3,4,3,1,2]
#Initalstate = np.array([Initalstate])

for x in range(1,dayf+1):
    
    #print(range(len(Fishes)))
    
    for i in range(len(Fishes)):
        if Fishes[i] != 0:
                Fishes[i] -= 1
       
        
        else:
            
            Fishes[i] = 6
            Fishes.append(8)
            
            #Fishes[i] = np.where((Fishes[i] == '0'), '6', Fishes[i])
            
    day += 1
    
    
print(day)
print(len(Fishes))

#%%

import sys
import numpy as np

with open('Day6Input.txt') as f:
    Fishes = f.read()

def get_fish():
    fish = np.array([int(x) for x in Fishes.readline().split(",")])
    ret_val = np.zeros((9,), dtype=np.longlong)
    for i in range(9):
        ret_val[i] = np.count_nonzero(fish == i)
    return ret_val


def main():
    fish = get_fish()
    for i in range(256):
        reproducing_fish = fish[0]
        # | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        # | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        fish[0:8] = fish[1:9]
        # | 0 |
        # | 6 |
        fish[6] += reproducing_fish
        # | 0 |
        # | 8 |
        fish[8] = reproducing_fish
    
    print("Total number of fish:\t" + str(fish.sum()))

if __name__ == "__main__":
    ans = main()
    
print(ans)

#%%

import numpy as np
with open('Day6Input.txt','r') as f: 
    rawData=f.read()
data=rawData.strip()
data=np.array(data.split(','),dtype=int)

def reproduce(initial,days):
    fishes=np.zeros(9,dtype=int)
    for i in range(fishes.shape[0]):
        fishes[i]=len(np.where(initial==i)[0])
    for d in range(days):
        zeroTo6=fishes[:7]
        seven8=fishes[7:]
        newFish=zeroTo6[0]
        zeroTo6=np.roll(zeroTo6,-1)
        zeroTo6[-1]+=seven8[0]
        seven8=np.roll(seven8,-1)
        seven8[-1]=newFish
        fishes=np.concatenate((zeroTo6,seven8))
    return fishes

# Part 1
print("Part 1 result {}".format(np.sum(reproduce(data, 80))))

# Part 2
print("Part 2 result {}".format(np.sum(reproduce(data, 256))))

#%%

def calc_fish(data, days):
    fish = [0] * 9
    for elm in data:
        fish[elm] += 1
    for _ in range(days):
        num_zero = fish[0]
        fish[:-1] = fish[1:]
        fish[8] = num_zero
        fish[6] += num_zero
    return sum(fish)

if __name__ == "__main__":
    data = np.loadtxt("Day6Input.txt", delimiter=",", dtype=int)         
    print(calc_fish(data, 80)) 
    print(calc_fish(data, 256))

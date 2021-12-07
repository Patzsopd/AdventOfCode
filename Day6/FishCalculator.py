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

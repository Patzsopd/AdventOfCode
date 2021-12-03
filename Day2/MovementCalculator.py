# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 07:39:30 2021

@author: Pat Zazzaro
"""

import os
import matplotlib.pyplot as plt
print(os.getcwd())
print()

#Getting Data from website
DataMove = open("Data2.txt","r")
content = DataMove.readlines()
my_list = [line.rstrip('\n') for line in content]
DataMove.close()

    
list_num = [int(sub.split(" ")[1]) for sub in my_list]
#print(list_str)
#print(list_num)


Depthiny = [] # Start Depth at Zero for plotting
HorPosinx = [] # Start Horizontal Position at Zero for plotting

Depth = 0
HorPos = 0

# Day 2 Part 1

for x in my_list:
    
    direction, value1 = x.split()
    value = int(value1) # turns str into int
        
    if direction == "forward":
        HorPos += value
        
        HorPosinx.append(HorPos)
        Depthiny.append(Depth)
    elif direction == "up":
        Depth -= value
        
        HorPosinx.append(HorPos)
        Depthiny.append(Depth)
    elif direction == "down":
        Depth += value
        
        HorPosinx.append(HorPos)
        Depthiny.append(Depth)
    else:
        print("Unknown input, check file")


ans = Depth*HorPos

print('This is the answer to part 1')
print(f'Your Horiztonal Postion is: {HorPos}')
print(f'Your Depth is: {Depth}')
print(f'Final Answer: {ans}')
print()

# Part 2 of Day 2

# Resetting graph parameters
Depthiny2 = [] # Start Depth at Zero for plotting
HorPosinx2 = [] # Start Horizontal Position at Zero for plotting

# Reset inital parameters
Depth2 = 0
HorPos2 = 0
aim = 0

for x in my_list:
    direction, value1 = x.split()
    value = int(value1)
    
    if direction == "forward":
        HorPos2 += value
        Depth2 += aim*value
        
        HorPosinx2.append(HorPos2)
        Depthiny2.append(Depth2)
    elif direction == "up":
        aim -= value
        
        HorPosinx2.append(HorPos2)
        Depthiny2.append(Depth2)
    elif direction == "down":
        aim += value
        
        HorPosinx2.append(HorPos2)
        Depthiny2.append(Depth2)
    else:
        print("Invalid Input, Please Check file")
        

ans2 = HorPos2*Depth2

print('This is the answer to part 2')
print(f'Your Horiztonal Postion is: {HorPos2}')
print(f'Your Depth is: {Depth2}')
print(f'Final Answer: {ans2}')
print()

Depthiny.reverse()
Depthiny2.reverse()

#plotting for fun
plt.plot(HorPosinx,Depthiny)
plt.plot(HorPosinx2,Depthiny2)
plt.title('Submarine Journey for the Keys (Part 1 vs Part 2)')
plt.xlabel('Horizontal Position')
plt.ylabel('Depth under water')
plt.show()
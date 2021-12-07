# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:11:21 2021

@author: Pat Zazzaro
"""

f = open("Day5input.txt", "r")
data = f.readlines()
f.close()

vent_ends = []
field = []

for line in data:
    pos1, pos2 = line.split("\n")[0].split(" -> ")
    pos1 = pos1.split(",")
    pos2 = pos2.split(",")
    
    vent_ends.append([[int(pos1[0]), int(pos1[1])], [int(pos2[0]), int(pos2[1])]])

#print(vent_ends)

# Creates the list to count where the vents are
for x in range(1000):
    new_col = []
    for y in range(1000):
        new_col.append(0)
    field.append(new_col)

# Function to analysis data, goes line by line
def add_vent(field, pos1, pos2):
    """Add the vent cells between pos1 and pos2 to the field."""
    
    x1 = pos1[0] # pulls from input for position 1
    y1 = pos1[1]
    
    x2 = pos2[0] # pulls from input for position 2
    y2 = pos2[1]
    
    # Straight lines (Part 1)
    if x1 == x2:
        if y1>y2:
            
            while y1>=y2:
                field[x1][y1] += 1
                y1 -= 1
                
        elif y1<y2:
            
            while y1<=y2:
                field[x1][y1] += 1
                y1 += 1
                
    elif y1==y2:
        
        if x1>x2:
            while x1>=x2:
                field[x1][y1] += 1
                x1 -= 1
                
        elif x1<x2:
            
            while x1<=x2:
                field[x1][y1] += 1
                x1 += 1
                
    # Diagonal lines (Part 2)
    
    
    elif x1>x2 and y1>y2:
        while x1>=x2:
            field[x1][y1] += 1
            x1 -= 1
            y1 -= 1
            
    elif x1>x2 and y1<y2:
        while x1>=x2:
            field[x1][y1] += 1
            x1 -= 1
            y1 += 1
            
    elif x1<x2 and y1>y2:
        while x1<=x2:
            field[x1][y1] += 1
            x1 += 1
            y1 -= 1
            
    elif x1<x2 and y1<y2:
        while x1<=x2:
            field[x1][y1] += 1
            x1 += 1
            y1 += 1
    
    return field

def count_overlaps(field):
    """Count the overlaping vent cells in the field."""
    
    overlaps = 0
    
    for x in range(len(field)):
        for cell in field[x]:
            if cell > 1:
                overlaps += 1
                
    return overlaps

def solution(field, vent_ends):
    """Find the solution for Day 5, Part 1 and Part 2."""
    
    for ends in vent_ends:
        field = add_vent(field, ends[0], ends[1])
        
    solution = count_overlaps(field)
    
    return solution

print(solution(field, vent_ends))
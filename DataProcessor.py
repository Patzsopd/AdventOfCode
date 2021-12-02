# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:38:42 2021

@author: Pat Zazzaro
"""

# Part 1 of Day 1
Data = open("Data.txt","r")
content = Data.read()
listofnumbers = content.split("\n")
Data.close()

#test situation
#Datatest = open("Datatest.txt","r")
#content1 = Datatest.read().splitlines()
#Datatest.close()

listlength = len(listofnumbers)
#listlength1 = len(content1)


def inc(x): 
    
    numcount = 0
    
    for i in range(listlength-1):
        prevint = int(x[i])
        currentint = int(x[i+1])
        
        if prevint < currentint:
            numcount+=1
    
    return numcount


if __name__ == "__main__":
    ans4one = inc(listofnumbers)
    
print(ans4one)

        
# Part 2 of Day 1


def incby3(y):
    
    num1count = 0
    
    for i in range(listlength-3):
        
        prevint = int(y[i]) + int(y[i+1]) + int(y[i+2])
        currentint = int(y[i+1]) + int(y[i+2]) + int(y[i+3])
        
        if prevint < currentint:
            num1count += 1
            
    return num1count

if __name__ == "__main__":
    ans4two = incby3(listofnumbers)
    
print (ans4two)
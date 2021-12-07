# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np


#Input our data from website

# Getting Bingo Call Data
with open('BingoCallout.txt') as f:
    Calldata = f.read()

Calldata.split(",")
inp = [int(x.strip()) for x in Calldata.split(",")]

Board = open("BingoBoard.txt","r").read().split()
BoardData = Board[1:]

fixed_bingo_boards = []
idx = 0

for x in range(100):
    fixed_bingo_boards.append([])

for i in BoardData:
    fixed_bingo_boards[idx].append(i)
    if len(fixed_bingo_boards[idx]) == 25:
        idx += 1



## Solution (ABove is my trying to understand wtf is going on)
b = [l.split(',') if i == 0 else l.split('\n') for i, l in enumerate(open('input4.txt','r').read().strip().split('\n\n'))]
inp = np.array(b.pop(0), dtype='int')
a = []

for l in b:
  t = []
  for w in l:
    t.append(w.split())
  a.append(t)
a = np.array(a, dtype='int')

#

def bingo(i, a, part):
  m = np.zeros((a.shape[:]))
  won = set()
  for j,n in enumerate(i):
    for k,o in enumerate(a):
      for l in range(len(o)):
        if n in o[l,:]:
          # found number in row and mark it:
          m[k, l, [h for h,f in enumerate(o[l,:]) if f == n][0]] = 1
        if n in o[:, l]:
          # found number in column and mark it:
          m[k, [h for h,f in enumerate(o[:,l]) if f == n][0], l] = 1
        if part == 1 and (sum(m[k, l, :]) == len(o) or sum(m[k, :, l]) == len(o)):
          return n * sum([o[s, g] for s,f in enumerate((m == 0)[k]) for g,h in enumerate(f) if h == True])
        if part == 2 and (sum(m[k, l, :]) == len(o) or sum(m[k, :, l]) == len(o)):
          won.add(k)
        if part == 2 and len(won) == len(a):
          return n * sum([o[s, g] for s,f in enumerate((m == 0)[k]) for g,h in enumerate(f) if h == True])
      
# Part 1
part = 1
print('Part 1 result is:', bingo(inp, a, part))
# Part 2
part = 2
print('Part 2 result is', bingo(inp, a, part))
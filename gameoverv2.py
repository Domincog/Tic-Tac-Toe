# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:16:52 2021

@author: DIncognito22
"""

def checkrows(board):
    x = 0
    o = 0
    for i in range(3):
        if board[i] == 'x':
            x = x+1
        elif board[i] == 'o':
            o=o+1
        if x==3 or o==3:
            return True
    x = 0
    o = 0
    for i in range(3):
        i = i + 3
        if board[i] == 'x':
            x = x+1
        elif board[i] == 'o':
            o=o+1
        if x==3 or o==3:
            return True
    x = 0
    o = 0
    for i in range(3):
        i = i + 6
        if board[i] == 'x':
            x = x+1
        elif board[i] == 'o':
            o=o+1
        if x==3 or o==3:
            return True 
    else:
        return False
    
def checkcols(board):
    x = 0
    o = 0
    placeholder = 0
    placeholder2 = placeholder
    for i in range(3):
        for i in range(3):
            if placeholder2 == placeholder:
                finder = placeholder2
                placeholder2 = placeholder + 1
            
            
            if board[finder] == 'x':
                x = x+1
            elif board[finder] == 'o':
                o=o+1
            if x==3 or o==3:
                return True
            
            finder = finder + 3
        placeholder = placeholder + 1
        x = 0
        o = 0
    return False

def diagonals(board):
    if board[0]=='x' and board[4]=='x' and board[8]=='x':
        return True
    elif board[0]=='o' and board[4]=='o' and board[8]=='o':
        return True
    elif board[2]=='x' and board[4]=='x' and board[6]=='x':
        return True
    elif board[2]=='o' and board[4]=='o' and board[6]=='o':
        return True
    else:
        return False
    
def fullboard2(board):
    for i in board:
        if i!='o' and i!='x':
            return False
    return True

def gameover(board):
    if fullboard2(board)==True or diagonals(board)==True or checkrows(board)==True or checkcols(board)==True:
        return True
    else:
        return False
    
#Checks to see if a piece was already played
def isplayed(y, check):
    if y[check] == 'o' or y[check] == 'x':
        return True
    else:
        return False
# gameovertest = ['o', 'o', 'o', 3 , 'x', 'o', 'o', 'o', 'x']
# gameovertest2 = ['o', 'o', 'o', 4, 'x', 'x', 7, 8, 'x']
# print(gameover(gameovertest2))



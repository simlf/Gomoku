#!/usr/bin/env python3

import sys
import random

sizeGame = 20
start = 0

def printBoard(board):
    for row in board:
        print(row)

def randomPlay(board):
    i = random.randint(0, sizeGame - 1)
    j = random.randint(0, sizeGame - 1)
    while board[i][j] != '-':
        i = random.randint(0, sizeGame - 1)
        j = random.randint(0, sizeGame - 1)
    return i, j

def fillTheBoard(board):
    line = input().split(',')
    while line[0] != 'DONE':
        if int(line[2]) == 1:
            board[int(line[1])][int(line[0])] = 'O'
        else:
            board[int(line[1])][int(line[0])] = 'X'
        line = input().split(',')
    return board

def check_direction(board, y, x):
    nb = 0
    size = 0
    max = 4
    tmp = 0
    if board[y][x + 1] == '1' or board[y][x + 2] == '1':
        while (nb < max):
            if (board[y][x + nb] == '-' and max <= 4):
                max += 1
                tmp = x + nb
            if (board[y][x + nb] == '1'):
                size += 1
            nb += 1
        if (max == 5 and size == 4):
            return (y, tmp)
        elif (size == 4 and board[y][x + nb] != '2'):    
            return (y, x + nb)
        elif (size == 4 and x - 1 >= 0 and board[y][x - 1] == '-'):
            return (y, x - 1)
    elif board[y + 1][x] == '1':
        while (nb < max):
            if (board[y + nb][x] == '1'):
                size += 1
            nb += 1
        if (size == 4):
            return (y + nb, x)
    return (-1, -1)

def play():
    board = [['-']*(sizeGame + 1) for i in range(sizeGame + 1)]
    y = 0
    x = 0
    while 1:
        line = input().split(' ')
        if line[0] == 'BEGIN':
            start = 1
            board[4][4] = 'O'
            print("%d,%d" % (4, 4), flush=True)
        elif line[0] == 'END':
            return 84
        elif line[0] == 'TURN' or line[0] == 'BOARD':
            if line[0] == 'BOARD':
                board = fillTheBoard(board)
            else:
                line = line[1].split(',')
                board[int(line[1])][int(line[0])] = 'X'
            board[0][0] = '1'
            board[1][0] = '1'
            board[2][0] = '1'
            board[3][0] = '1'
            value = False
            for y in range(sizeGame):
                if value == True:
                    break
                for x in range(sizeGame):
                    if board[y][x] == '1':
                        print("hello")
                        i, j = check_direction(board, y, x)
                        print(i, j)
                        value = True
                        y = sizeGame
                        break
            if (i >= 0 or j >= 0):
                board[i][j] = '1'
            printBoard(board)
            print("%d,%d" % (j, i), flush=True)
        if line[0] == 'RESTART':
            break
    return 0

def start():
    start = input().split(' ')
    if len(start) == 2 and start[0] == 'START' and 5 <= int(start[1]) <= 20:
        print("OK", flush=True)
        sizeGame = int(start[1]) - 1
        return 0
    else:
        print("ERROR", flush=True)
    return 0


def main():
    tmp = 0
    if start() == 0:
        while tmp == 0:
            tmp = play()
    return 0



if __name__ == "__main__":
    main()


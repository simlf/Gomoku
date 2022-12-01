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
            board[int(line[1])][int(line[0])] = '1'
        else:
            board[int(line[1])][int(line[0])] = '2'
        line = input().split(',')
    return board

def check_direction(board, y, x, sizeGame):
    nb = 0
    size = 0
    max = 4
    tmp = 0
    if  ((x + 1 < sizeGame) and (board[y][x + 1] == '1' or board[y][x + 2] == '1')):
        while (nb < max):
            if (board[y][x + nb] == '-' and max <= 4):
                max += 1
                tmp = x + nb
            if (board[y][x + nb] == '1'):
                size += 1
            nb += 1
        if (max == 5 and size == 4):
            return (y, tmp)
        elif ((x + nb <= sizeGame) and (size == 4 and board[y][x + nb] != '2')):
            return (y, x + nb)
        elif (size == 4 and x - 1 >= 0 and board[y][x - 1] == '-'):
            return (y, x - 1)
    elif ((y + 1 < sizeGame) and (board[y + 1][x] == '1' or board[y + 2][x] == '1')):
        while (nb < max):
            if (board[y+ nb][x] == '-' and max <= 4):
                max += 1
                tmp = y + nb
            if (board[y + nb][x] == '1'):
                size += 1
            nb += 1
        if (max == 5 and size == 4):
            return (tmp, x)
        elif ((y + nb <= sizeGame) and (size == 4 and board[y + nb][x] != '2')):
            return (y + nb, x)
        elif (size == 4 and y - 1 >= 0 and board[y - 1][x] == '-'):
            return (y - 1, x)
    elif ((x + 1 < sizeGame and y + 1 < sizeGame) and (board[y + 1][x + 1] == '1' or board[y + 2][x + 2] == '1')):
        while (nb < max):
            if (board[y + nb][x + nb] == '-' and max <= 4):
                max += 1
                tmp = x + nb
                tmp2 = y + nb
            if (board[y + nb][x + nb] == '1'):
                size += 1
            nb += 1
        if (max == 5 and size == 4):
            return (tmp2, tmp)
        if (size == 4 and x + nb <= sizeGame and y + nb <= sizeGame and board[y + nb][x + nb] == '-'):
            return (y + nb, x + nb)
        if (size == 4 and y >= 1 and x >= 1 and board[y - 1][x - 1] == '-'):
            return (y - 1, x - 1)
    elif ((x - 1 < sizeGame and y + 1 < sizeGame) and (board[y + 1][x - 1] == '1' or board[y + 2][x - 2] == '1')):
        while (nb < max):
            if (board[y + nb][x - nb] == '-' and max <= 4):
                max += 1
                tmp = x - nb
                tmp2 = y + nb
            if (board[y + nb][x - nb] == '1'):
                size += 1
            nb += 1
        if (max == 5 and size == 4):
            return (tmp2, tmp)
        if (size == 4 and x - nb <= sizeGame and y + nb <= sizeGame and board[y + nb][x - nb] == '-'):
            return (y + nb, x - nb)
        if (size == 4 and y >= 1 and x >= 1 and board[y - 1][x - 1] == '-'):
            return (y - 1, x - 1)


    return (-1, -1)

def defend(board, sizeGame):
    value = False
    nb = 0
    size = 0
    for y in range(sizeGame):
        if value == True:
            break
        for x in range(sizeGame):
            max = 3
            if board[y][x] == '2':
                # vertical
                if (x + 1 < sizeGame and board[y][x + 1] == '2' or (x + 2 < sizeGame and board[y][x + 2] == "2")):
                    while (nb < max):
                        if (board[y][x + nb] == '-' and max <= 3):
                            max += 1
                            tmp = x + nb
                        if (board[y][x + nb] == '2'):
                            size += 1
                        nb += 1
                    if (max == 4 and board[y][tmp] == '-'):
                        return (y, tmp)
                    if (max == 3):
                        if (x + nb > sizeGame):
                            if (board[y][x - 1] == '-'):
                                return (y, x - 1)
                            return (-1, -1)
                        elif (x - 1 >= 0 and board[y][x + nb] != '-'):
                            if (board[y][x - 1] == '-'):
                                return (y, x - 1)
                            return (-1, -1)
                        elif (board[y][x + nb] == '-'):
                            return (y, x + nb)
                # horizontal
                if (y + 1 < sizeGame and board[y + 1][x] == '2' or (y + 2 < sizeGame and board[y + 2][x] == "2")):
                    while (nb < max):
                        if (board[y + nb][x] == '-' and max <= 3):
                            max += 1
                            tmp = y + nb
                        if (board[y + nb][x] == '2'):
                            size += 1
                        nb += 1
                    if (max == 4 and board[tmp][x] == '-'):
                        return (tmp, x)
                    if (max == 3):
                        if (y + nb > sizeGame):
                            if (board[y - 1][x] == '-'):
                                return (y - 1, x)
                            return (-1, -1)
                        elif (y - 1 >= 0 and board[y + nb][x] != '-'):
                            if (board[y - 1][x] == '-'):
                                return (y - 1, x)
                            return (-1, -1)
                        elif (board[y + nb][x] == '-'):
                            return (y + nb, x)
                # diagonal left
                if (y + 1 <= sizeGame and x + 1 <= sizeGame and board[y + 1][x + 1] == '2' or (y + 2 < sizeGame and x + 2 < sizeGame and board[y + 2][x + 2] == "2")):
                    while (nb < max):
                        if (y + nb <= sizeGame and x + nb <= sizeGame and board[y + nb][x + nb] == '-' and max <= 3):
                            max += 1
                            tmp = y + nb
                            tmp2 = x + nb
                        if (y + nb <= sizeGame and x + nb <= sizeGame and board[y + nb][x + nb] == '2'):
                            size += 1
                        nb += 1
                    if (max == 4 and board[tmp][tmp2] == '-' and size == 3):
                        return (tmp, tmp2)
                    if (max == 3 and size == 3):
                        if (y + nb <= sizeGame and x + nb <= sizeGame):
                            if (board[y + nb][x + nb] == '-'):
                                return (y + nb, x + nb)
                            elif (y - 1 >= 0 and x >= 0 and board[y - 1][x - 1] == '-'):
                                return (y - 1, x - 1)
                        if ((y + nb > sizeGame or x + nb > sizeGame) and (y - 1 >= 0 and x - 1 >= 0) and board[y - 1][x - 1] == '-'):
                            return (y - 1, x - 1)
                # diagonal left
                if (y + 1 <= sizeGame and x - 1 <= sizeGame and board[y + 1][x - 1] == '2' or (y + 2 < sizeGame and x + 2 < sizeGame and board[y + 2][x + 2] == "2")):
                    while (nb < max):
                        if (y + nb <= sizeGame and x - nb <= sizeGame and board[y + nb][x - nb] == '-' and max <= 3):
                            max += 1
                            tmp = y + nb
                            tmp2 = x - nb
                        if (y + nb <= sizeGame and x - nb <= sizeGame and board[y + nb][x - nb] == '2'):
                            size += 1
                        nb += 1
                    if (max == 4 and board[tmp][tmp2] == '-' and size == 3):
                        return (tmp, tmp2)
                    if (max == 3 and size == 3):
                        if (y + nb <= sizeGame and x - nb <= sizeGame):
                            if (board[y + nb][x - nb] == '-'):
                                return (y + nb, x - nb)
                            elif (y - 1 >= 0 and x >= 0 and board[y - 1][x - 1] == '-'):
                                return (y - 1, x + 1)
                        if ((y + nb > sizeGame or x - nb > sizeGame) and (y - 1 >= 0 and x - 1 >= 0) and board[y - 1][x + 1] == '-'):
                            return (y - 1, x + 1)
                value = True
                y = sizeGame
                break
    return (-1, -1)

def play():
    board = [['-']*(sizeGame + 1) for i in range(sizeGame + 1)]
    y = 0
    x = 0
    while 1:
        i = -1
        j = -1
        line = input().split(' ')
        if line[0] == 'BEGIN':
            start = 1
            i,j = randomPlay(board)
            board[i][j] = '1'
            print("%d,%d" % (j,i), flush=True)
        elif line[0] == 'END':
            return 84
        elif line[0] == 'TURN' or line[0] == 'BOARD':
            if line[0] == 'BOARD':
                board = fillTheBoard(board)
            else:
                line = line[1].split(',')
                board[int(line[1])][int(line[0])] = '2'
            value = False
            for y in range(sizeGame):
                if value == True:
                    break
                for x in range(sizeGame):
                    if board[y][x] == '1':
                        i, j = check_direction(board, y, x, sizeGame)
                        value = True
                        y = sizeGame
                        break
            if (i < 0 and j < 0):
                i, j = defend(board, sizeGame)
            if (i < 0 and j < 0):
                i, j = randomPlay(board)
            board[i][j] = '1'
            print("%d,%d" % (j,i), flush=True)
        if line[0] == 'RESTART':
            break
    return 0

def start():
    global sizeGame
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
    try:
        main()
    except KeyboardInterrupt:
        print("ERROR", flush=True)
        exit(0)

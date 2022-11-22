#!/usr/bin/env python3

import sys
import random

sizeGame = 20
start = 0

#  if len(sys.argv) > 1:
#         readFrom = open(sys.argv[1], "r")
#     for line in readFrom:
#         input = line.strip("\n").split(" ")
#         if (input[0] == "START"):
#             commands.start(int(input[1]))
#         elif (input[0] == "BEGIN"):
#             commands.begin()
#         elif (input[0] == "TURN"):
#             splitted = input[1].split(",")
#             commands.turn(int(splitted[0]), int(splitted[1]))
#         elif (input[0] == "BOARD"):
#             commands.board()
#         elif (input[0] == "INFO"):
#             commands.info(input[1], input[2])
#         elif (input[0] == "ABOUT"):
#             commands.about()
#         elif (input[0] == "END"):
#             commands.end()
#         elif (input[0] == "DEBUG"):
#             commands.debug(input[1])

#     exit(0)
def fillTheBoard(board):
    line = input().split(',')
    while line[0] != 'DONE':
        if int(line[2]) == 1:
            board[int(line[1])][int(line[0])] = 'O'
        else:
            board[int(line[1])][int(line[0])] = 'X'
        line = input().split(',')
    return board

def play():
    board = [['-']*(sizeGame + 1) for i in range(sizeGame + 1)]
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
            i = random.randint(0, sizeGame - 1)
            j = random.randint(0, sizeGame - 1)
            board[i][j] = 'O'
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


#!/usr/bin/env python3

import random
import sys

import Utils
class Commands:
    def __init__(self):
        self._size = 0
        self._board = [[]]

    def createBoard(self, size):
        self._size = size
        self._board = [[0 for x in range(self._size)] for y in range(self._size)]

    def end(self):
        quit()

    def start(self, size):
        if (size < 5):
            print("ERROR", flush=True)
        else:
            self.createBoard(size)
            print("OK", flush=True)

    def begin(self):
        print("10, 10", flush=True)

    def turn(self, x, y):
        i = random.randint(0, self.size)
        j = random.randint(0, self.size)
        print(i,", ", j, flush=True)

    def board(self):
        while True:
            line = sys.stdin.readline().rstrip("\n")

            if line == "DONE":
                Utils.printBoard(self._board)
                print("10, 10", flush=True)
                break
            else:
                instruction = line.split(",")
                self._board[int(instruction[0])][int(instruction[1])] = int(instruction[2])

    def info(key, value):
        pass

    def about(self):
        pass

    def debug(self, str):
        print(str, flush=True)

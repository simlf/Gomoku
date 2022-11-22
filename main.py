#!/usr/bin/env python3

import sys
from src.Commands import Commands

if __name__ == "__main__":
    commands = Commands()
    readFrom = sys.stdin

    if len(sys.argv) > 1:
        readFrom = open(sys.argv[1], "r")

    for line in readFrom:
        input = line.strip("\n").split(" ")

        if (input[0] == "START"):
            commands.start(int(input[1]))
        elif (input[0] == "BEGIN"):
            commands.begin()
        elif (input[0] == "TURN"):
            splitted = input[1].split(",")
            commands.turn(int(splitted[0]), int(splitted[1]))
        elif (input[0] == "BOARD"):
            commands.board()
        elif (input[0] == "INFO"):
            splitted = input[1].split(" ")
            commands.info(input[1])
        elif (input[0] == "ABOUT"):
            commands.about()
        elif (input[0] == "END"):
            commands.end()
        elif (input[0] == "DEBUG"):
            commands.debug(input[1])

    exit(0)

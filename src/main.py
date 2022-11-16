from src.Commands import Commands

if __name__ == "__main__":
    commands = Commands()

    for line in str.stdin:
        input = line.split(" ")
        if (input[0] == "START"):
            commands.start(int(input[1]))
        elif (input[0] == "BEGIN"):
            commands.begin()
        elif (input[0] == "TURN"):
            commands.turn(int(input[1]), int(input[2]))
        elif (input[0] == "BOARD"):
            commands.board(input[1])
        elif (input[0] == "INFO"):
            commands.info(input[1], input[2])
        elif (input[0] == "ABOUT"):
            commands.about()
        elif (input[0] == "END"):
            commands.end()

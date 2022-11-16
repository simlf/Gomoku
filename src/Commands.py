class Commands:
    def __init__(self):
        self.size = 0
        self.board = [[]]

    def createBoard(self, size):
        self.size = size
        self.board = [[0 for x in range(size)] for y in range(size)]

    def end():
        exit(0)

    def start(self, size):
        if (size < 5):
            print("ERROR", flush=True)
        self.createBoard(size)

        print("OK", flush=True)

    def begin():
        print("10, 10", flush=True)

    def turn(x, y):
        print("10, 10", flush=True)

    def board(self, str):
        for line in str.splitlines():
            if (line == "DONE"):
                print("9, 9", flush=True)
            input = line.split(",")
            x = int(input[0])
            y = int(input[1])
            if (input[2] == "1"):
                self.Board[x][y] = 1
            elif (input[2] == "2"):
                self.Board[x][y] = 2

    def info(key, value):
        pass

    def about():
        pass

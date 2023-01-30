from Board import *
from Game import *
from Node import *

def main():
    print("AI is Red, You are Blue\n")

    while True:
        try:
            row = int(input("Enter number of rows for board size: "))
            col = int(input("Enter number of columns for board size: "))
            plies = int(input("Enter number of plies: "))

        except ValueError:
            print("Input must be an integer")
            continue

        else:
            print("")
            size = (row, col)
            board = Board(size=size)
            game = Game(board=board, plies=plies)
            game.run()
            break

if __name__ == "__main__":
    main()
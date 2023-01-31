from Board import *
from MyGame import *

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
            # board.addEdge(0,0,"top",True,"A")
            # board.addEdge(0,0,"right",True,"A")
            # board.addEdge(0,0,"left",True,"A")
            # board.addEdge(0,0,"bot",True,"A")

            # board.addEdge(0,1,"top",True,"A")
            # board.addEdge(0,1,"right",True,"A")
            # board.addEdge(0,1,"bot",True,"A")
            # board.addEdge(0,1,"left",True,"A")

            # board.addEdge(0,2,"top",True,"A")

            # board.addEdge(1,0,"bot",True,"A")
            # board.addEdge(1,0,"left",True,"A")
            # board.addEdge(1,0,"right",True,"A")

            # board.addEdge(1,1,"right",True,"A")

            # board.addEdge(1,2,"right",True,"A")

            # board.board[0][0].value = 2
            # board.board[0][1].value = 3
            # board.board[0][2].value = 5
            # board.board[1][0].value = 1
            # board.board[1][1].value = 4
            # board.board[1][2].value = 3


            game = Game(board=board, plies=plies)
            game.minmax_search()
            break

if __name__ == "__main__":
    main()
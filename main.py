from Board import *

def main():
    size = int(input("Enter board size: "))
    board = Board(size=size)
    
    player = "A"
    print(board)

    while not board.gameOver():
        row = int(input("Row: "))
        col = int(input("Col: "))
        edge = str(input("Edge: "))

        board.addEdge(row, col, edge, True, player)
        print(board)

        if player == "A": # change player
            player = "B"
        else:
            player = "A"

        print(board.getScore())

    print(board)

if __name__ == "__main__":
    main()

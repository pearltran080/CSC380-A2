from Board import *
from Node import *

class Game(object):
    def __init__(self, board: Board, plies: int):
        self.plies = plies
        self.playerScore = 0
        self.compScore = 0
        self.board = board

    def minimax(self, depth: int, max: bool):
        if depth == self.plies:
            return

        score = self.board.getScore()

        if (self.board.gameOver):
            return score

        if (max):
            # move where ever available
            for i in range(self.board.rows):
                for j in range(self.board.cols):
                    if (not self.board.board[i][j].top.edge):
                        self.board.addEdge(i, j, "top", True, "A")
                    elif (not self.board.board[i][j].bot.edge):
                        self.board.addEdge(i, j, "bot", True, "A")
                    elif (not self.board.board[i][j].left.edge):
                        self.board.addEdge(i, j, "left", True, "A")
                    elif (not self.board.board[i][j].right.edge):
                        self.board.addEdge(i, j, "right", True, "A")


    def moveAI(self):
        # if currDepth == self.plies:
        #     return
        return [0, 0, "right"]

    def run(self):
        player = "A"

        while not self.board.gameOver():
            if (player == "A"):           # AI's turn
                aiMove = self.moveAI()
                print("AI MOVED row: {} col: {} edge: {}".format(aiMove[0], aiMove[1], aiMove[2]))
                self.board.addEdge(aiMove[0], aiMove[1], aiMove[2], True, player)
                player = "B"

            else:                       # player's turn
                print("YOUR TURN")
                while True:
                    try:
                        row = int(input("Row: "))
                        col = int(input("Col: "))
                        edge = str(input("Edge: "))

                    except ValueError:
                        # type checking
                        print("Required types = \nrow:int, col:int \nedge:str (top, bot, right, left)")
                        continue

                    else:
                        # input checking
                        if (row >= self.board.rows):
                            print("Row out of bounds")
                            continue
                        elif (col >= self.board.cols):
                            print("Column out of bounds")
                            continue

                        if (edge == "top" and not self.board.board[row][col].top.edge):
                            pass
                        elif (edge == "bot" and not self.board.board[row][col].bot.edge):
                            pass
                        elif (edge == "left" and not self.board.board[row][col].left.edge):
                            pass
                        elif (edge == "right" and not self.board.board[row][col].right.edge):
                            pass
                        else:
                            print(edge + " edge is already placed here, try again")
                            continue

                        # place edge for player
                        self.board.addEdge(row, col, edge, True, player)
                        print("YOUR MOVE")
                        player = "A"
                        break

            print(self.board)
            print("AI Score: {}, Your Score: {}".format(self.board.getPlayerScore("A"), self.board.getPlayerScore("B")))
            print("")

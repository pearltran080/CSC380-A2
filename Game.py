from Board import *

class Game(object):
    def __init__(self, board: Board, plies: int):
        self.plies = plies
        self.board = board

    def max_value(self):
        if (self.plies == 0) or (self.board.gameOver()):
            return (self.board.getScore(), None)
        
        maxVal = -5000
        maxMove = None

        for i, j, edge in self.board.expand():
            tempBoard = self.board.getBoardCopy()
            tempBoard.addEdge(i, j, edge, True, "A")
            nextState = Game(tempBoard, self.plies - 1)
            value, _ = nextState.min_value()

            if maxVal < value:
                maxVal = value
                maxMove = (i, j, edge)
        
        return maxVal, maxMove  # maxMove = move to get to the state with maxVal

    def min_value(self):
        if (self.plies == 0) or (self.board.gameOver()):
            return (self.board.getScore(), None)

        minVal = 5000
        minMove = None

        for i, j, edge in self.board.expand():
            tempBoard = self.board.getBoardCopy()
            tempBoard.addEdge(i, j, edge, True, "B")
            nextState = Game(tempBoard, self.plies - 1)
            value, _ = nextState.max_value()

            if minVal > value:
                minVal = value
                minMove = (i, j, edge)
        
        return minVal, minMove  # minMove = move to get to the state with minVal

    def minimax(self):
        value, move = self.max_value()
        return move

    def run(self):
        player = "A"

        while not self.board.gameOver():
            if (player == "A"):         # AI's turn
                aiMove = self.minimax()
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
                            print(edge + " is either already placed or is not an edge name. try again")
                            continue

                        # place edge for player
                        self.board.addEdge(row, col, edge, True, player)
                        print("YOUR MOVE")
                        player = "A"
                        break

            print(self.board)
            print("AI Score: {}, Your Score: {}".format(self.board.getPlayerScore("A"), self.board.getPlayerScore("B")))
            print("")
        print("GAME OVER")
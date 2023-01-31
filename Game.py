from Board import *

class Game(object):
    def __init__(self, board: Board, plies: int):
        self.plies = plies
        self.playerScore = 0
        self.compScore = 0
        self.board = board

    def minimax(self, depth: int, maxTurn: bool):
        score = self.board.getScore()
        # base cases: reached target plies, game is over
        if (depth == self.plies) or (self.board.gameOver()):
            return score

        if (maxTurn):
            bestScore = -5000

            for i in range(self.board.rows):
                for j in range(self.board.cols):
                    if (not self.board.board[i][j].top.edge):
                        self.board.addEdge(i, j, "top", True, "A")
                        bestScore = max(bestScore, self.minimax(depth=depth + 1, maxTurn=False))
                        self.board.addEdge(i, j, "top", False, "A")

                    if (not self.board.board[i][j].bot.edge):
                        self.board.addEdge(i, j, "bot", True, "A")
                        bestScore = max(bestScore, self.minimax(depth=depth + 1, maxTurn=False))
                        self.board.addEdge(i, j, "bot", False, "A")

                    if (not self.board.board[i][j].left.edge):
                        self.board.addEdge(i, j, "left", True, "A")
                        bestScore = max(bestScore, self.minimax(depth=depth + 1, maxTurn=False))
                        self.board.addEdge(i, j, "left", False, "A")

                    if (not self.board.board[i][j].right.edge):
                        self.board.addEdge(i, j, "right", True, "A")
                        bestScore = max(bestScore, self.minimax(depth=depth + 1, maxTurn=False))
                        self.board.addEdge(i, j, "right", False, "A")

            return bestScore
        
        else:
            bestScore = 5000

            for i in range(self.board.rows):
                for j in range(self.board.cols):
                    if (not self.board.board[i][j].top.edge):
                        self.board.addEdge(i, j, "top", True, "B")
                        bestScore = min(bestScore, self.minimax(depth=depth + 1, maxTurn=True))
                        self.board.addEdge(i, j, "top", False, "B")

                    if (not self.board.board[i][j].bot.edge):
                        self.board.addEdge(i, j, "bot", True, "B")
                        bestScore = min(bestScore, self.minimax(depth=depth + 1, maxTurn=True))
                        self.board.addEdge(i, j, "bot", False, "B")

                    if (not self.board.board[i][j].left.edge):
                        self.board.addEdge(i, j, "left", True, "B")
                        bestScore = min(bestScore, self.minimax(depth=depth + 1, maxTurn=True))
                        self.board.addEdge(i, j, "left", False, "B")

                    if (not self.board.board[i][j].right.edge):
                        self.board.addEdge(i, j, "right", True, "B")
                        bestScore = min(bestScore, self.minimax(depth=depth + 1, maxTurn=True))
                        self.board.addEdge(i, j, "right", False, "B")

            return bestScore

    def moveAI(self):
        bestScore = -5000
        move = [-1, -1, ""]

        for i in range(self.board.rows):
            for j in range(self.board.cols):
                if (not self.board.board[i][j].top.edge):
                    self.board.addEdge(i, j, "top", True, "A")
                    moveScore = self.minimax(depth=0, maxTurn=False)
                    self.board.addEdge(i, j, "top", False, "A")
                    if (moveScore > bestScore):
                        bestScore = moveScore
                        move = [i, j, "top"]

                if (not self.board.board[i][j].bot.edge):
                    self.board.addEdge(i, j, "bot", True, "A")
                    moveScore = self.minimax(depth=0, maxTurn=False)
                    self.board.addEdge(i, j, "bot", False, "A")
                    if (moveScore > bestScore):
                        bestScore = moveScore
                        move = [i, j, "bot"]

                if (not self.board.board[i][j].left.edge):
                    self.board.addEdge(i, j, "left", True, "A")
                    moveScore = self.minimax(depth=0, maxTurn=False)
                    self.board.addEdge(i, j, "left", False, "A")
                    if (moveScore > bestScore):
                        bestScore = moveScore
                        move = [i, j, "left"]

                if (not self.board.board[i][j].right.edge):
                    self.board.addEdge(i, j, "right", True, "A")
                    moveScore = self.minimax(depth=0, maxTurn=False)
                    self.board.addEdge(i, j, "right", False, "A")
                    if (moveScore > bestScore):
                        bestScore = moveScore
                        move = [i, j, "right"]
        
        return move

    def run(self):
        player = "B"

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

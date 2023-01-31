from Board import *

class Game(object):
    def __init__(self, board: Board, plies: int):
        self.board = board
        self.plies = plies

    def max_value(self, a, b):
        if self.board.gameOver() or self.plies <= 0:
            return (self.board.getScore(), None)

        bestScore = float('-inf')
        bestMove = None

        for i, j, edge in self.board.actions():
            newBoard = self.board.copyBoard()
            newBoard.addEdge(i, j, edge, True, 'A')
            nextGameState = Game(newBoard, self.plies-1)
            minVal, _ = nextGameState.min_value(a,b)
            if minVal > bestScore:
                bestScore = minVal
                bestMove = (i, j, edge)
                a = max(a, bestScore)
            if bestScore >= b:
                return bestScore, bestMove

        return bestScore, bestMove
    
    def min_value(self, a, b):
        if self.board.gameOver() or self.plies <= 0:
            return (self.board.getScore(), None)

        bestScore = float('inf')
        bestMove = None

        for i, j, edge in self.board.actions():
            newBoard = self.board.copyBoard()
            newBoard.addEdge(i, j, edge, True, 'B')
            nextGameState = Game(newBoard, self.plies-1)
            maxVal, _ = nextGameState.max_value(a,b)
            if maxVal < bestScore:
                bestScore = maxVal
                bestMove = (i, j, edge)
                b = min(b, bestScore)
            if bestScore <= a:
                return bestScore, bestMove
        
        return bestScore, bestMove

    def minmax_search(self):
        player = 'A'
        while not self.board.gameOver():
            if (player == "A"):           # AI's turn
                aiScore, aiMove = self.max_value(float('-inf'),float('inf'))
                print(f"AI1 MOVED row: {aiMove[0]} col: {aiMove[1]} edge: {aiMove[2]}")
                self.board.addEdge(aiMove[0], aiMove[1], aiMove[2], True, player)
                player = "B"

            else:                       # player's turn
                aiScore, aiMove = self.max_value(float('-inf'),float('inf'))
                print(f"AI2 MOVED row: {aiMove[0]} col: {aiMove[1]} edge: {aiMove[2]}")
                self.board.addEdge(aiMove[0], aiMove[1], aiMove[2], True, player)
                player = "A"
                '''
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
                    '''

            print(self.board)
            print("AI1 Score: {}, AI2 Score: {}".format(self.board.getPlayerScore("A"), self.board.getPlayerScore("B")))
            print("")
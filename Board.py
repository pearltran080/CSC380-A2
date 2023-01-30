import random

class colors:
    BLUE = '\033[1;34m'
    CYAN = '\033[1;36m'
    GREEN = '\033[1;32m'
    RED = '\033[1;31m'
    YELLOW = '\033[1;33m'
    MAGENTA = '\033[1;35m'

    BLUE_HIGHLIGHT = '\033[0;37;44m'
    CYAN_HIGHLIGHT = '\033[0;37;46m'
    GREEN_HIGHLIGHT = '\033[0;37;42m'
    RED_HIGHLIGHT = '\033[0;37;41m'
    YELLOW_HIGHLIGHT = '\033[0;37;43m'
    MAGENTA_HIGHLIGHT = '\033[0;37;45m'

    BLUE_UNDERLINE = '\033[4;34m'
    CYAN_UNDERLINE = '\033[4;36m'
    GREEN_UNDERLINE = '\033[4;32m'
    RED_UNDERLINE = '\033[4;31m'
    YELLOW_UNDERLINE = '\033[4;33m'
    MAGENTA_UNDERLINE = '\033[4;35m'

    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HIGHLIGHT = '\033[0;37;47m'

class Edge(object):
    def __init__(self):
        self.edge = False

class Box(object):
    def __init__(self, value: int, top: Edge, bot: Edge, left: Edge, right: Edge):
        self.value = value
        self.top = top
        self.bot = bot
        self.left = left
        self.right = right
        self.owner = None

class Board(object):
    def __init__(self, size: tuple()):
        self.rows = size[0]
        self.cols = size[1]
        self.board = []

        for i in range(self.rows):

            row = []
            for j in range(self.cols):
                topEdge = None
                botEdge = Edge()
                leftEdge = None
                rightEdge = Edge()
                if i == 0:
                    topEdge = Edge()
                else:
                    topEdge = self.board[i-1][j].bot

                if j == 0:
                    leftEdge = Edge()
                else:
                    leftEdge = row[-1].right

                box = Box(value=random.randrange(1, 6), top=topEdge, bot=botEdge, left=leftEdge, right=rightEdge)
                row.append(box)

            self.board.append(row)

    def addEdge(self, row: int, col: int, edge: str, flag: bool, player: str):
        # add new edge
        if (edge == "top"):
            self.board[row][col].top.edge = flag
        elif (edge == "bot"):
            self.board[row][col].bot.edge = flag
        elif (edge == "left"):
            self.board[row][col].left.edge = flag
        elif (edge == "right"):
            self.board[row][col].right.edge = flag
        else:
            raise ValueError

        self.setOwner(row, col, player)

        # set owner for adjacent box if new edge completes more than one box
        if (edge == "top" and row != 0):
            self.setOwner(row-1, col, player)
        elif (edge == "bot" and row != self.rows-1):
            self.setOwner(row+1, col, player)
        elif (edge == "left" and col != 0):
            self.setOwner(row, col-1, player)
        elif (edge == "right" and col != self.cols-1):
            self.setOwner(row, col+1, player)

    # set owner of box as current player if all 4 edges are placed
    def setOwner(self, row: int, col: int, player: str):
        if (self.board[row][col].top.edge and self.board[row][col].bot.edge and self.board[row][col].left.edge and self.board[row][col].right.edge):
            self.board[row][col].owner = player
        else:
            self.board[row][col].owner = None

    # scoring function for minimax
    def getScore(self):
        score = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if (self.board[i][j].owner == "A"):
                    score += self.board[i][j].value
                elif (self.board[i][j].owner == "B"):
                    score -= self.board[i][j].value
        return score

    # if all boxes are claimed (no more lines can be placed), then game is over
    def gameOver(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if (self.board[i][j].owner == None):
                    return False
        return True

    def getPlayerScore(self, player: str):
        score = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if (self.board[i][j].owner == player):
                    score += self.board[i][j].value
        return score

    def __repr__(self):
        return str(self)

    def __str__(self):
        s = ''
        for i in range(self.rows):
            for j in range(self.cols):      # print top horizontal edges
                if (self.board[i][j].top.edge):
                    s += "+-"
                else:
                    s += "+ "
                
                if (j == self.cols-1):
                    s += "+\n"

            for j in range(self.cols):      # print vertical edges and numbers
                if (self.board[i][j].left.edge):
                    s += "|"
                else:
                    s += " "
                
                if (self.board[i][j].owner == "A"):
                    s += colors.RED_HIGHLIGHT + str(self.board[i][j].value) + colors.ENDC
                elif (self.board[i][j].owner == "B"):
                    s += colors.BLUE_HIGHLIGHT + str(self.board[i][j].value) + colors.ENDC
                else:
                    s += str(self.board[i][j].value)

                if (j == self.cols-1):
                    if (self.board[i][j].right.edge):
                        s += "|"
                    else:
                        s += " "
                    s += "\n"

            if (i == self.rows-1):          # print bottom horizontal edges
                for j in range(self.cols):
                    if (self.board[i][j].bot.edge):
                        s += "+-"
                    else:
                        s += "+ "
                s += "+"
        
        return s
        
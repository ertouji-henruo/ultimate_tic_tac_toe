import numpy as np


class Game:
    def __init__(self):
        """initialise board"""
        self.history = []
        single = np.zeros(9).reshape(3, 3)
        self.board = []
        self.overall = np.zeros(9).reshape(3, 3)
        for i in range(0, 9):
            self.board.append(single)
        self.board = np.array(self.board)
        self.board = self.board.reshape(3, 3, 3, 3)

    def getMoves(self):
        """returns all legal moves as a list of tuples"""
        moves = []
        if len(self.history) != 0:
            lastMove = self.history[len(self.history) - 1]
            for i in range(0, self.board.shape[2]):
                for j in range(0, self.board.shape[3]):
                    if self.board[lastMove[2], lastMove[3], i, j] == 0:
                        if self.overall[lastMove[2], lastMove[3]] == 0:
                            moves.append((lastMove[2], lastMove[3], i, j))
            if len(moves) != 0:
                return moves
        if len(self.history) == 0 or len(moves) == 0:
            for i in range(0, self.overall.shape[0]):
                for j in range(0, self.overall.shape[1]):
                    if self.overall[i, j] == 0:
                        for k in range(0, self.board.shape[2]):
                            for l in range(0, self.board.shape[3]):
                                if self.board[i, j, k, l] == 0:
                                    moves.append((i, j, k, l))

            return moves

    def makeMove(self, pos):
        """makes the input move"""
        player = self.turn()
        self.board[pos[0], pos[1], pos[2], pos[3]] = player
        self.checkOverBoard((pos[0], pos[1]))
        self.history.append(pos)

    def undoMove(self, pos):
        """undo input move"""
        self.board[pos[0], pos[1], pos[2], pos[3]] = 0
        self.overall[pos[0], pos[1]] = 0
        self.history.remove(pos)

    def turn(self):
        """returns which player's turn it is"""
        nCount = 0
        cCount = 0
        player = 0
        for i in range(0, self.board.shape[0]):
            for j in range(0, self.board.shape[1]):
                for k in range(0, self.board.shape[2]):
                    for l in range(0, self.board.shape[3]):
                        if self.board[i, j, k, l] == 1:
                            nCount += 1
                        elif self.board[i, j, k, l] == 2:
                            cCount += 1
        if nCount > cCount:
            player = 2
        else:
            player = 1
        return player

    def checkOverBoard(self,  boardPos):
        """checks the 3x3 boards if they are finished and updates overall accordingly"""
        players = [1, 2]
        board = self.board[boardPos[0], boardPos[1]]
        for player in players:
            # checks rows and columns (for arbitrary grid size )
            for i in range(0, board.shape[0]):
                if list(board[i]).count(player) == board.shape[0]:
                    self.overall[boardPos[0], boardPos[1]] = player
                    return

            transposed = np.transpose(board)
            for i in range(0, transposed.shape[0]):
                if list(transposed[i]).count(player) == transposed.shape[0]:
                    self.overall[boardPos[0], boardPos[1]] = player
                    return

            # checks diagonals (not for arbitrary grid size)
            if (board[0, 0] == board[1, 1] == board[2, 2] == player) or (board[0, 2] == board[1, 1] == board[2, 0] == player):
                self.overall[boardPos[0], boardPos[1]] = player
                return

            # checks for draw
            incompleteCount = 0
            for i in range(0, board.shape[0]):
                for j in range(0, board.shape[1]):
                    if board[i, j] == 0:
                        incompleteCount += 1
            if incompleteCount == 0:
                self.overall[boardPos[0], boardPos[1]] = 3
                return

        return

    def checkOver(self):
        """returns True if game is over"""
        players = [1, 2]
        for player in players:
            # checks rows and columns (for arbitrary grid size )
            for i in range(0, self.overall.shape[0]):
                if list(self.overall[i]).count(player) == self.overall.shape[0]:
                    return True, 1, player
            transposed = np.transpose(self.overall)
            for i in range(0, transposed.shape[0]):
                if list(transposed[i]).count(player) == transposed.shape[0]:
                    return True, 1, player

            # checks diagonals (not for arbitrary grid size)
            if (self.overall[0, 0] == self.overall[1, 1] == self.overall[2, 2] == player) \
                    or (self.overall[0, 2] == self.overall[1, 1] == self.overall[2, 0] == player):
                return True, 1, player

            # checks for draw
            incompleteCount = 0
            for i in range(0, self.overall.shape[0]):
                for j in range(0, self.overall.shape[1]):
                    if self.overall[i, j] == 0:
                        incompleteCount += 1
            if incompleteCount == 0:
                return True, 0, 0

        return False,




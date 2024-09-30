import numpy as np


class Game:
    def __init__(self):
        """"initialise board"""
        self.board = np.zeros(9).reshape(3, 3)
        self.history = []

    def getMoves(self):
        """returns all legal moves as a list of tuples"""
        moves = []
        for i in range(0, self.board.shape[0]):
            for j in range(0, self.board.shape[1]):
                if self.board[i, j] == 0:
                    moves.append((i, j))
        return moves

    def makeMove(self, pos):
        """makes the input move"""
        player = self.turn()
        self.board[pos[0], pos[1]] = player

    def undoMove(self, pos):
        self.board[pos[0], pos[1]] = 0

    def turn(self):
        """returns which player's turn it is"""
        nCount = 0
        cCount = 0
        player = 0
        for i in range(0, self.board.shape[0]):
            for j in range(0, self.board.shape[1]):
                if self.board[i, j] == 1:
                    nCount += 1
                elif self.board[i, j] == 2:
                    cCount += 1
        if nCount > cCount:
            player = 2
        else:
            player = 1
        return player

    def checkOver(self):
        """returns True if game is over"""
        players = [1, 2]
        for player in players:

            # checks rows and columns (for arbitrary grid size )
            for i in range(0, self.board.shape[0]):
                if list(self.board[i]).count(player) == self.board.shape[0]:
                    return True, 1, player
            transposed = np.transpose(self.board)
            for i in range(0, transposed.shape[0]):
                if list(transposed[i]).count(player) == transposed.shape[0]:
                    return True, 1, player

            # checks diagonals (not for arbitrary grid size)
            if (self.board[0, 0] == self.board[1, 1] == self.board[2, 2] == player) \
                    or (self.board[0, 2] == self.board[1, 1] == self.board[2, 0] == player):
                return True, 1, player

            # checks for draw
            if len(self.getMoves()) == 0:
                return True, 0, 0

        return False,


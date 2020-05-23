import numpy as np

class Board:
    """
    This class represents a board. It only allows the placement and removal of
    queens from the board. When adding queen,s it does not try to match the
    N-Queen problem conditions; instead, to check wheter a position is
    unreachable by any of the currently placed queens, it provides the
    is_valid() method.

    Since the class is used for the N-Queens problem, it is always initialized
    as a square board.
    """

    def __init__(self,size):
        """
        Instantiates a square board of the given size.

        Arguments:
            size {int} -- The number of tiles on each axis
        """
        self.size = size
        self.board = np.reshape([0]*(size**2),(size,size))
        self.occupied = set()
        self.removed = set()

    def place_queen(self, row, col):
        """
        Allows you to place a queen at the given row and column of the board.
        Invalid inputs result in no changes.

        Arguments:
            row {int} -- The row position indexed from 0
            col {int} -- The column position indexed from 1
        """
        if row >=0 and row< self.size and col >=0 and col <= self.size:
            self.board[row][col] = 1
            self.occupied.add((row,col))

    def remove_queen(self, row, col):
        """
        Allows you to remove a queen at the given row and column of the board.
        Invalid inputs result in no changes.

        Arguments:
            row {int} -- The row position indexed from 0
            col {int} -- The column position indexed from 1
        """
        if row >=0 and row< self.size and col >=0 and col <= self.size:
            self.board[row][col] = 0
            self.occupied.remove((row,col))
            self.removed.add((row,col))


    def is_valid(self, row, col):
        """
        When solving the N-Queens problem, this method can be used to check
        wheter the position you are trying to insert a queen at is valid. That
        is, it checks to make sure the position is unreachable by the pieces
        placed so far.

        Arguments:
            row {int} -- The row indexed from 0
            col {int} -- The column indexed from 0

        Returns:
            boolean -- True if the position is valid and False otherwise
        """
        if row >=0 and row< self.size and col >=0 and col <= self.size:
            return (self._horizontal_valid(row)
                    and self._vertical_valid(col)
                    and self._diagonal_1_valid(row,col)
                    and self._diagonal_2_valid(row,col))
        else:
            return False



    def _horizontal_valid(self,row):
        """
        Checks occupied positions against given row to see if another
        queen occupies it.

        Arguments:
            row {int} -- The row indexed from 0

        Returns:
            boolean -- True is the row is a valid spot to place a queen and
            False otherwise
        """
        for coord in self.occupied:
            if coord[0] == row:
                return False
        return True

    def _vertical_valid(self,col):
        """
        Checks occupied positions against given column to see if another
        queen occupies it.

        Arguments:
            column {int} -- The column indexed from 0

        Returns:
            boolean -- True is the row is a valid spot to place a queen and
            False otherwise
        """
        for coord in self.occupied:
            if coord[1] == col:
                return False
        return True

    def _diagonal_1_valid(self,row,col):
        """
        Checks occupied positions against the given row and column to see if another
        queen occupies the TLBR diagonal for the given position.

        Arguments:
            row {int} -- The row indexed from 0
            column {int} -- The column indexed from 0

        Returns:
            boolean -- True is the row is a valid spot to place a queen and
            False otherwise
        """
        diagonal_diff = row-col  # all coordinates on this diagonal have the same x-y difference
        for coord in self.occupied:
            if coord[0]-coord[1] == diagonal_diff:
                return False
        return True

    def _diagonal_2_valid(self,row,col):
        """
        Checks occupied positions against the given row and column to see if another
        queen occupies the TRBL diagonal for the given position.

        Arguments:
            row {int} -- The row indexed from 0
            column {int} -- The column indexed from 0

        Returns:
            boolean -- True is the row is a valid spot to place a queen and
            False otherwise
        """
        diagonal_diff = row+col # all coordinates on this diagonal have the same x+y sum
        for coord in self.occupied:
            if coord[0]+coord[1] == diagonal_diff:
                return False
        return True


import sys
import pygame
from internal.board import Board
from internal.reference import *


def _solve(n, col, brd, rows_visited, window):
    """
    This function uses recursive backtracking to solve the N-Queens problem. In
    each call assuming there are queens left to arrange, the algorithm makes a
    choice and checks all possible outcomes that stem from it. If none of the
    outcomes are desirable, the algorithm backtracks and makes a different
    choice.

    This function will return the first solution it finds and since it assumes
    the value of n is valid, there will always be a solution.

    Arguments:
        n {int} -- Number of queens left
        col {int} -- Current column in which queen must be placed starting index
        0
        brd {Board} -- The board on which the queen must be placed
        rows_visited {set} -- A set of the rows that have queens in them so we
        can avoid them
        window {Surface} -- Pygame window to visualize the process in

    Returns:
        Board -- The solution board
    """
    if n == 0:
        return brd
    else:
        for i in range(brd.size):
            if i not in rows_visited:  # Skip occupied rows
                if brd.is_valid(i, col):

                    # Choose
                    rows_visited.add(i)
                    brd.place_queen(i, col)

                    draw(window, brd)
                    pygame.time.wait(100)

                    # Explore
                    result = _solve(n - 1, col + 1, brd, rows_visited, window)

                    if result is not None:
                        return result
                    else:
                        # Unchoose
                        rows_visited.remove(i)
                        brd.remove_queen(i, col)
                        draw(window, brd)
                        pygame.time.wait(100)


def draw(window, board):
    """
    This function is called to draw the current board. It will draw a
    checkerboard from the board object such that all occupied squares are shown
    in green and all removed pieces are shown in red. This function resets
    removed pieces on the board to set() after visualizing the removals. This
    has been done to dynamically show the removal of queens.

    Arguments:
        window {Surface} -- Pygame window in which things are visualized
        board {Board} -- The board to draw
    """
    window.fill((0, 0, 55))

    alt = 0
    for i in range(board.size):
        for j in range(board.size):

            # alt is used to alternate tile colours
            if (j, i) not in board.occupied and (
                    j, i) not in board.removed and alt == 0:
                window.blit(WHITE_SQ, (i * TILE_SIZE, j * TILE_SIZE))
            else:
                if (j, i) in board.occupied:
                    window.blit(GREEN_SQ, (i * TILE_SIZE, j * TILE_SIZE))
                elif (j, i) in board.removed:
                    window.blit(RED_SQ, (i * TILE_SIZE, j * TILE_SIZE))

            alt = abs(alt - 1)
        if board.size % 2 == 0:
            alt = abs(alt - 1)

    board.removed = set()
    pygame.display.update()


def solve(n):
    """
    This function solves the N-Queen problem of size n. Assumes the input value
    of n is valid

    Arguments:
        n {int} -- The size of the N-Queens problem. Must be > 3
    """
    # Adjust window to accomodate all the tiles
    WIN_WIDTH = n * TILE_SIZE
    WIN_HEIGHT = n * TILE_SIZE
    WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    # Before starting
    brd = Board(n)
    draw(WINDOW, brd)
    pygame.time.wait(2000)

    # The remaining process including the final result
    result = _solve(n, 0, brd, set(), WINDOW)
    draw(WINDOW, result)
    pygame.time.wait(3000)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = sys.argv[1]
        try:
            n = int(n)
            if n > 3:
                solve(n)
            else:
                print("n must be more than 3")
        except ValueError:
            print("Please input numbers")
    else:
        print("You need to specify the problem size")

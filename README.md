# N-Queens
The eight queens puzzle was a problem where 8 queens had to be placed on a chess board such that no queen could reach any other queen on the board. This problem, however, is a very specific example of the more general N-Queens problem which as you might have guessed involves attempting to place N queens (N > 3) on a board of size NxN such that no queen can can reach any other queen.

## Solving the Problem
The N-Queens puzzle is not impossible to solve by hand, but after a certain value of N, it understandably becomes more frustarating to find a solution. The solution to this? Use computers to explore every single arrangement!

## Algorithm and Visualizer
Okay, so technically we don't explore every single solution but we do explore a lot of them. In this case, my program is using a recursive backtracking algorithm to make choices about where to place queens at each step and then following through on all the branching outcomes to arrive at a solution. The algorithm can be hard to understand through text though, so I made this visualizer to help! 

The visualizer provides a way to "see" the algorithm at work. It uses `PyGame` to show choices made (by the algorithm) in green and choices discarded in red. The result is a changing checkerboard pattern that demonstrates exactly how recursive backtracking works to solve the N-Queens problem on any N value!

## Using

### Before Running (Assuming you have pip)
* Run `pip install pygame` in the terminal
* Run `pip install numpy`

**Note:** I am using `pygame 1.9.6`, `numpy 1.18.4` and `python 3.7.4`

### Running
Clone the rep and run `visualize.py` in the terminal with n passed as the argument.
On Windows CMD this looks like:

`>python visualize.py 8`

Which will visualize the solution to the N-Queens Problem for N=8

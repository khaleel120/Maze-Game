# Maze-Game
          This is a simple python program, which creates a random maze and the user should find the possible path from one end(start) to the other end (end) of the maze to finish the game.

Working:
            In this  project, we uses the depth-first search (DFS) algorithm to generate a random maze. The algorithm starts at a random cell of the grid, and "carves" a path through the grid by visiting unvisited neighboring cells and marking them as part of the solution path.

The code is divided into several functions:

‘build_grid’: which creates a 20x20 grid of cells on the Pygame screen. It uses the ‘pygame.draw.line’ function to draw the lines of the grid.
‘push_up’, ‘push_down’, ‘push_left’, and ‘push_right’: These functions are used to visually update the screen as the algorithm carves out the maze. They draw a blue rectangle on the screen to indicate that a cell has been visited.
‘single_cell’: This function is used to draw a green rectangle on the screen to indicate the starting cell of the maze.
‘backtracking_cell’: This function is used to draw a blue rectangle on the screen to indicate the cells that have been visited but not part of the solution path.
‘solution_cell’: This function is used to draw a yellow rectangle on the screen to indicate the cells that are part of the solution path.
‘carve_out_maze’: This is the main function that implements the depth-first search algorithm. It starts at a random cell, and repeatedly chooses a random unvisited neighboring cell and "carves" a path to that cell. This function is called inside the main game loop.
It starts with the ‘carve_out_maze’ function, which sets a single cell as the starting point of the maze and starts a loop which continues until the stack (which is keeping track of the current position) is empty. In each iteration, the function chooses one of the unvisited neighboring cells at random and "carves" a path to that cell by updating the screen and adding the new cell to the stack and visited list. It continues in this fashion until the stack is empty, indicating that all possible path has been traversed.

The solution of the maze is found by starting from the end point and following the path back to the start, each step is indicated by calling ‘solution_cell’ function

It allows the user to repeat the generation of a maze if the user presses any key. And it stops the game when the user presses the escape key or closes the window. 

1. Import random, set up the global variable for grid size and number of ships, and initialize a 2D array to represent the grid.

2. drawBoard function
-The funciton for drawBoard should display the grid, print column headers, and print rows with rowheaders.
-The numbers 0-9 should be displayed along the top and left sides of the drawing to easily identify each column/row on the board.  Each square should display one of four possible characters
 -A dot ‘.‘ for any square that does not contain a ship and that has not yet been called out by the user at the keyboard
 -The letter ‘S’ to represent one of the 5 ships on the board
 -The letter ‘O’ to represent a row/column that was called out but did not contain a ship (i.e., a “miss”)
 -The letter ‘X’ to represent a row/column that was called out and there was a ship there (i.e., a “hit”)

3. setupBoard function
-initizlize's the grid with ships placed randomly
 #place a ship only if the cell is empty

4. checkHitorMiss function
-If a square contains a ship, the square on the board should be updated to show a 'X' and the string returned should be 'HIT'
-Otherwise, that square on the board should be updated to an ‘O’ to represent a miss and return the String “MISS”

5. isGameOver function
-assess the board to see if all th ships on that board have been hit/sunk

6. Main function
-main game loop
-gets user input for row and column
-checks hit or miss and display result
-end the code with running the main function to start the game

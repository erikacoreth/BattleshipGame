import random
#global variable for grid size and number of ships
grid_size = 10
num_ships = 5


#initialize a 2D array to represent the grid
grid = [['.']*grid_size for i in range(grid_size)]

#display the grid
def drawBoard(board):
    #print column headers
    print('  ', end='')
    for col in range(grid_size):
        print(f'{col}', end='')
    print()

    #print rows with rowheaders
    for row in range(grid_size):
        print(f'{row}', end='')
        for col in range(grid_size):
            print(f'{board[row][col]}', end='')
        print()

 #initizlize the grid with ships placed randomly
def setupBoard(board):
    ships_placed = 0
    while ships_placed < num_ships:
        randomRow = random.randint(0, grid_size - 1)
        randomCol = random.randint(0, grid_size - 1)

        #place a ship only if the cell is empty
        if board[randomRow][randomCol] == '.':
            board[randomRow][randomCol] = 'S'
            ships_placed += 1


def hitOrMiss(board, row, col):
    if board[row][col] == 'S':
        board[row][col] = 'X' #hit
        return 'HIT'
    elif board[row][col] == 'X': #already hit
        return 'HIT'
    else:
        board[row][col] = 'O' #miss
        return 'MISS'

#check if the game is ocer (all ships are hit)
def isGameOver(board):
    for row in board:
        if 'S' in row: #if theres still an 'S', (ship), the game isnt over
            return False
    return True

#main game loop
def main():
    setupBoard(grid)
    print('Welcome to Battleship!')

    #Game loop
    while not isGameOver(grid):
        drawBoard(grid)

        #get user input for row and column
        try:
            col = int(input('Enter a column (0-9): '))
            if col < 0 or col >= grid_size:
                print('Invalid column. Try again.')
                continue

            row = int(input('Enter a row (0-9): '))
            if row < 0 or row >= grid_size:
                print('Invalid row. Try again.')
                continue

        except ValueError:
            print('Invalid input. Please enter an integer.')
            continue

        #check hit or miss and display result
        result = hitOrMiss(grid, row, col)
        print(result)

    drawBoard(grid)
    print('GAME OVER! All ships have been sunk.')

#run the main function to start the game
main()



board1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

for i in range(len(board)):
    print("Enter 0 for empty square")
    for j in range(len(board[0])):
        board[i][j] = int(input(f'Enter value for [{i}, {j}]: '))

def display_board(x):
    '''
    Make the board look like this:
    The 0-8 before each row are indexes of the board
    board = [
        0[7,8,0,|4,0,0,1,2,0],
        1[6,0,0,|0,7,5,0,0,9],
        2[0,0,0,|6,0,1,0,7,8],
        -------------------
        3[0,0,7,|0,4,0,2,6,0],
        4[0,0,1,0,5,0,9,3,0],
        5[9,0,4,0,6,0,0,0,5],
        -------------------
        6[0,7,0,3,0,0,0,1,2],
        7[1,2,0,0,0,7,4,0,0],
        8[0,4,9,2,0,6,0,0,7]
    ]
    '''    
    for i in range(len(x)):
        if i % 3 == 0 and i != 0: #Does something for every 3rd row without including the first row(indexed 0)
            print('------------------------------')

        for q in range(len(x[0])):
            if q % 3 == 0 and q != 0: #Does something for every 3rd column without including the first column(indexed 0)
                print('|', end = ' ')
            if q == 8:
                print(x[i][q])
            else:
                print(str(x[i][q]) + ' ', end = ' ') 


def find_empty(x):
    '''Finds the first empty spot in the board and returns its values'''
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 0:
                return (i, j)  # row, col

    return None

def valid(x, num, pos):
    # Check row
    for i in range(len(x[0])):
        if x[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(x)):
        if x[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if x[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(x):
    '''Use recursive backtracking to solve the sudoku'''
    find = find_empty(x)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(x, i, (row, col)):
            x[row][col] = i # Set the number

            if solve(x): # Check if it is a solution
                return True 

            x[row][col] = 0 # Reset the number

    return False


solve(board)
print('Sudoku Solver')


#Check if the board is solved.
if not solve(board):
    print('No solution found for the sodoku board below:')
    display_board(board)
else:
    print('Solution found')
    display_board(board)
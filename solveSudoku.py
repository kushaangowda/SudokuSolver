board = [
    [0,3,5,0,0,0,0,0,6],
    [0,0,0,0,7,0,8,0,0],
    [0,0,1,0,0,9,0,0,0],
    [9,2,0,0,0,0,0,7,8],
    [0,5,0,0,0,0,0,2,0],
    [3,0,0,0,0,0,5,0,0],
    [0,0,0,5,0,0,0,1,0],
    [0,9,4,0,0,0,2,0,0],
    [0,0,0,6,0,7,0,0,4]
]

def display_board(bd):
    for i in range(0,9):
        if i == 3 or i == 6:
            print("- - - - - - - - - - - - - ")
        for j in range(0,9):
            if j == 3 or j == 6:
                print(" | ", end="")
            if j == 8:
                print(bd[i][j])
            else:
                print(str(bd[i][j]) + " ", end="")

def find_next_empty_cell(bd):
    for i in range(0,9):
        for j in range(0,9):
            if bd[i][j] == 0:
                return (i,j)
    return None

def solve_board(bd):
    find = find_next_empty_cell(bd)
    if find == None:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bd, i, (row, col)):
            bd[row][col] = i
            if solve_board(bd):
                return True
            bd[row][col] = 0
    return False

def valid(bd, num, pos):
    for i in range(0,9):
        if bd[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(0,9):
        if bd[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bd[i][j] == num and (i,j) != pos:
                return False

    return True


print('Welcome to Sudoku Solver')

print('\nGiven Board\n')
display_board(board)

solve_board(board)
print('\n\nSolved Board\n')
display_board(board)
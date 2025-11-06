def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1: return False
    for i, j in zip(range(row-1,-1,-1), range(col-1,-1,-1)):
        if board[i][j] == 1: return False
    for i, j in zip(range(row-1,-1,-1), range(col+1,n)):
        if board[i][j] == 1: return False
    return True

def solve(board, row, n):
    if row == n: return True
    if 1 in board[row]: return solve(board, row+1, n)
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, row+1, n): return True
            board[row][col] = 0
    return False

def n_queens(n, first_pos):
    board = [[0]*n for _ in range(n)]
    board[first_pos[0]][first_pos[1]] = 1
    if solve(board, 0, n): return board
    return None

def print_board(board):
    if not board:
        print("No solution")
        return
    for row in board:
        print(" ".join('Q' if x else '.' for x in row))

# Take user input
n = int(input("Enter size of board (n): "))
row = int(input(f"Enter row position of first queen (0 to {n-1}): "))
col = int(input(f"Enter column position of first queen (0 to {n-1}): "))

board = n_queens(n, (row, col))
print_board(board)


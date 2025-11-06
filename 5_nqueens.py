import time

def is_safe(board, row, column, size):
    for i in range(row):
        if board[i][column] or (column-(row-i))>=0 and board[i][column-(row-i)] \
           or (column+(row-i))<size and board[i][column+(row-i)]:
            return False
    return True

def solve(board, row, size):
    if row == size:
        return True
    for column in range(size):
        if is_safe(board, row, column, size):
            board[row][column] = 1
            if solve(board, row+1, size):
                return True
            board[row][column] = 0
    return False

size = int(input("Enter board size: "))
row = int(input(f"Enter row position (0 to {size-1}): "))
column = int(input(f"Enter column position (0 to {size-1}): "))

start = time.time()
board = [[0]*size for _ in range(size)]
board[row][column] = 1
solve(board, 0, size)
end = time.time()

for r in board:
    print(" ".join('Q' if x else '.' for x in r))
print("Time Taken:", format(end-start, '.6f'), "seconds")

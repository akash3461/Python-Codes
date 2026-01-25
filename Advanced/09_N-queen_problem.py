def is_safe(board, row, col, n):
    # Check previously placed queens
    for i in range(col):
        # Same row or diagonal check
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True


def solve_n_queens(board, col, n):
    # If all queens are placed, print the solution
    if col == n:
        print(board)
        return

    # Try placing queen in each row
    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve_n_queens(board, col + 1, n)


n = 4
board = [-1] * n

# Start solving the problem
solve_n_queens(board, 0, n)

'''
        OUTPUT:
[1, 3, 0, 2]
[2, 0, 3, 1]

'''
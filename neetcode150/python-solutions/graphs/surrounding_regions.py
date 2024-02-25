def surroundig_regions(board):
    ROWS = len(board)
    COLS = len(board[0])

    def capture(board, row, col):
        if not (0 <= row < ROWS and 0 <= col < COLS and board[row][col] == "O"):
            return

        board[row][col] = "T"

        capture(board, row - 1, col)
        capture(board, row, col - 1)
        capture(board, row + 1, col)
        capture(board, row, col + 1)

    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == "O" and (i in [0, ROWS - 1] or j in [0, COLS - 1]):
                capture(board, i, j)

    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == "O":
                board[i][j] = "X"

    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == "T":
                board[i][j] = "O"

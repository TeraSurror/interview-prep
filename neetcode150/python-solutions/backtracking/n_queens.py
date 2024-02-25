def n_queens(n):
    result = []
    board = ["." * n for i in range(n)]

    col = set()
    pos_diag = set()
    neg_diag = set()

    def dfs(row):
        if row == n:
            result.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in col or (row + c) in pos_diag or (row - c) in neg_diag:
                continue

            col.add(c)
            pos_diag.add(row + c)
            neg_diag.add(row - c)
            board[row][c] = "Q"

            dfs(row + 1)

            col.remove(c)
            pos_diag.remove(row + c)
            neg_diag.remove(row - c)
            board[row][c] = "."

    dfs(0)
    return result

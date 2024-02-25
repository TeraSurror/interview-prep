def word_search(board, word):
    result = True

    def dfs(grid, visited, row, col, letter_index):
        if letter_index >= len(word):
            return False

        if not is_valid_cell(grid, row, col):
            return False

        visited[row][col] = True

        if word[letter_index] == grid[row][col]:
            if letter_index == len(word) - 1:
                return True
            else:
                letter_index += 1
                return (
                    dfs(grid, visited, row + 1, col, letter_index)
                    or dfs(grid, visited, row - 1, col, letter_index)
                    or dfs(grid, visited, row, col - 1, letter_index)
                    or dfs(grid, visited, row, col + 1, letter_index)
                )
        else:
            return False

    def is_valid_cell(grid, row, col):
        return (
            0 <= row < len(grid)
            and 0 <= col < len(grid[0])
            and visited[row][col] == False
        )

    visited = [[False] * len(board[0])] * len(board)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                result = dfs(board, visited, i, j, 0)

    return result

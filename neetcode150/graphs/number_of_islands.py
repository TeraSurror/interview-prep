def num_islands(grid):
    def dfs(row, col):
        if not (
            0 <= row < ROWS
            and 0 <= col < COLS
            and visited[row][col] == False
            and grid[row][col] == "1"
        ):
            return

        visited[row][col] = True
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    result = 0
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = [[False] * COLS for i in range(ROWS)]

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "1":
                dfs(row, col)
                result += 1

    return result

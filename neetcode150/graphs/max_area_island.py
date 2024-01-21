def max_area_of_island(grid):
    result = 0

    visited = [[False] * len(grid[0]) for i in range(len(grid))]

    def dfs(grid, row, col):
        if not (
            0 <= row < len(grid)
            and 0 <= col < len(grid[0])
            and not visited[row][col]
            and grid[row][col] == 1
        ):
            return 0

        visited[row][col] = True

        return (
            1
            + dfs(grid, row + 1, col)
            + dfs(grid, row - 1, col)
            + dfs(grid, row, col + 1)
            + dfs(grid, row, col - 1)
        )

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and not visited[row][col]:
                result = max(result, dfs(grid, row, col))

    return result

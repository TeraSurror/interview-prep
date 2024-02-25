def pacific_atlantic(heights):
    result = []

    def dfs(heights, visited, row, col, pa, prev):
        if not (
            0 <= row < len(heights)
            and 0 <= col < len(heights[0])
            and visited[row][col] == False
            and heights[row][col] <= prev
        ):
            return False

        visited[row][col] = True

        if pa:
            if row == 0 or col == 0:
                print(row, col, "p")
                return True
        else:
            if row == len(heights) - 1 or col == len(heights[0]) - 1:
                print(row, col, "a")
                return True

        return (
            dfs(heights, visited, row + 1, col, pa, heights[row][col])
            or dfs(heights, visited, row - 1, col, pa, heights[row][col])
            or dfs(heights, visited, row, col + 1, pa, heights[row][col])
            or dfs(heights, visited, row, col - 1, pa, heights[row][col])
        )

    for row in range(len(heights)):
        for col in range(len(heights[0])):
            visited1 = [[False] * len(heights[0]) for i in range(len(heights))]
            visited2 = [[False] * len(heights[0]) for i in range(len(heights))]
            if dfs(heights, visited1, row, col, True, 1000001) and dfs(
                heights, visited2, row, col, False, 1000001
            ):
                result.append([row, col])

    return result

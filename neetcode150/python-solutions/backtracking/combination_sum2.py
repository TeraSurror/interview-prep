def combination_sum2(candidates, target):
    result = []
    candidates.sort()

    subsets = []

    def dfs(i, aim):
        if aim == 0:
            result.append(subsets[:])
            return

        if i >= len(candidates):
            return

        if aim - candidates[i] >= 0:
            subsets.append(candidates[i])
            dfs(i + 1, aim - candidates[i])
            subsets.pop()

        while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
            i += 1

        dfs(i + 1, aim)

    dfs(0, target)
    return result

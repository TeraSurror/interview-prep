def can_finish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}

    for course, pre in prerequisites:
        graph[course].append(pre)

    visited = set()

    def dfs(course):
        if course in visited:
            return False

        if len(graph[course]) == 0:
            return True

        visited.add(course)

        for pre in graph[course]:
            if not dfs(pre):
                return False

        visited.remove(course)
        graph[course] = []
        return True

    for c in range(numCourses):
        if not dfs(c):
            return False

    return True

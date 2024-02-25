def find_path(tickets):
    # initialize graph
    graph = {}

    # create graph
    for frm, to in tickets:
        if frm in graph:
            graph[frm].append(to)
        else:
            graph[frm] = [to]

    for key in graph.keys():
        graph[key].sort()

    # travese using bfs and go to the nodeoo
    def dfs(graph, result, start):
        if start in graph:
            destinations = graph[start][:]
            while destinations:
                curr = destinations[0]
                graph[start].pop(0)
                dfs(graph, result, curr)
                destinations = graph[start][:]

        result.append(start)

    result = []
    dfs(graph, result, "JFK")
    result.reverse()

    if len(result) != len(tickets) + 1:
        return []

    return result

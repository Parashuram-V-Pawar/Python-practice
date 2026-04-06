def has_cycle(graph):
    visited = set()
    path = set()

    def dfs(node):
        if node in path:
            return True
        if node in visited:
            return False

        visited.add(node)
        path.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        path.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False


graph = {
    0: [1],
    1: [2],
    2: [0]
}

print(has_cycle(graph))
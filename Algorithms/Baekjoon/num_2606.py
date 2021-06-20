c = int(input())
l = int(input())

graph = {i: [] for i in range(1, c+1)}

for i in range(1, l+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def BFS(graph, start):
    queue = [start]
    visited = []
    while queue:
        n = queue.pop(0)
        visited.append(n)
        for node in graph[n]:
            if node not in visited:
                queue.append(node)
    return visited

print(len(set(BFS(graph, 1)))-1)


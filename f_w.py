import math

def pythagorean_theorem(coord1, coord2):
    return math.sqrt(math.pow(coord2[0]-coord1[0], 2) + math.pow(coord2[1]-coord1[1], 2))

def graph_to_matrix(graph):
    matrix = [[math.inf] * len(graph) for i in range(len(graph))]
    parents = [[None] * len(graph) for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if j in graph[i][1]:
                matrix[i][j] = pythagorean_theorem(graph[i][0], graph[j][0])
                parents[i][j] = i
    return matrix, parents


def floyd_warshall(graph):
    matrix, parents = graph_to_matrix(graph)
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    parents[i][j] = parents[k][j]
    return matrix, parents

def floyd_warshall_path(parents, start, end):
    assert parents is not None, "There are no parents"
    path = []
    path.append(end)
    while start != end:
        end = parents[start][end]
        path.insert(0, end)
    return path

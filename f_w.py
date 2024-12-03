import math

def pythagorean_theorem(coord1, coord2):
    return math.sqrt(math.pow(coord2[0]-coord1[0], 2) + math.pow(coord2[1]-coord1[1], 2))

def graph_to_matrix(graph):
    matrix = [[math.inf] * len(graph) for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if j in graph[i][1]:
                matrix[i][j] = pythagorean_theorem(graph[i][0], graph[j][0])
    return matrix


def floyd_warshall(graph):
    matrix = graph_to_matrix(graph)
    parents = [[None] * len(graph) for i in range(len(graph))]
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i == j:
                    continue
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
                    parents[i][j] = k
    return matrix, parents

def floyd_warshall_path(parents, start, end):
    path = []
    node = parents[start][end]
    while node is not None:
        path.append(node)
        node = parents[start][node]
    path.append(start)
    path.reverse()
    path.append(end)
    return path

graph = [
        [(900, 45), [17, 21, 22]], #0
        [(70, 350), [2, 7, 19, 20]], #1
        [(140, 420), [1, 5, 9, 10, 20]], #2
        [(210, 70), [6, 8, 11, 22]], #3
        [(210, 210), [6, 7, 11, 12, 20]], #4
        [(210, 490), [2, 10, 21]], #5
        [(280, 140), [3, 4, 11, 20]], #6
        [(280, 280), [1, 4, 9, 12, 20]], #7
        [(350, 70), [3, 11]], #8
        [(350, 350), [2, 7, 10, 12, 13, 15]], #9
        [(350, 490), [2, 5, 9, 13, 14, 15]], #10
        [(420, 140), [3, 4, 6, 8, 12, 16, 17]], #11
        [(420, 280), [4, 7, 9, 11, 15, 17]], #12
        [(420, 420), [9, 10, 15]], #13
        [(490, 490), [10, 18, 15]], #14
        [(560, 420), [9, 10, 12, 13, 14, 17, 18]], #15
        [(630, 70), [11, 17]], #16
        [(630, 210), [11, 12, 15, 16, 18, 0]], #17
        [(700, 420), [14, 15, 17, 23]], #18
        [(70, 500), [1, 21]], #19
        [(70, 210), [1, 2, 4, 6, 7, 22]], #20
        [(450, 700), [5, 19, 0, 23]], #21
        [(45, 45), [0, 3, 20]], #22
        [(1225, 700), [18, 21]] #23
    ]

_, parents = floyd_warshall(graph)
path = floyd_warshall_path(parents, 0, 13)
path_reversed = floyd_warshall_path(parents, 13, 0)
print(path)
print(path_reversed)
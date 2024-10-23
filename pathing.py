import graph_data
import global_game_data
import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    #global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    #global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    graphData = graph_data.graph_data[global_game_data.current_graph_index]
    assert graph_data is not None
    targetFound = False
    startIndex = 0
    endLoop = False
    path = [] #path returned as list of nodes to visit
    currentIndex = startIndex
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    assert target_node is not None

    while not endLoop:
        #tracks if target has been found
        if (currentIndex == target_node):
            targetFound = True
        #tracks end loop
        if (currentIndex == len(graphData) - 1 and targetFound):
            endLoop = True
            break
        possibilities = graphData[currentIndex][1] #possibilities come from node neighbors
        #assign random next node
        nextNode = possibilities[random.randint(0,len(possibilities) - 1)]
        path.append(nextNode)
        currentIndex = nextNode
    assert path is not None
    assert path[len(path) - 1] == len(graphData) - 1
    return path


def get_dfs_path():
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    path = dfs_path_creation(0, target_node)
    graphData = graph_data.graph_data[global_game_data.current_graph_index]
    secondPath = dfs_path_creation(target_node, len(graphData) - 1)
    path = path + secondPath
    assert target_node in path
    assert len(graphData) - 1 in path
    for i in range (0, len(path) - 2):
        assert path[i+1] in graphData[path[i]][1], f"Path did not find {path[i+1]} in {graphData[path[i]][1]}"
    return path

def dfs_path_creation(start, end):
    graphData = graph_data.graph_data[global_game_data.current_graph_index]
    assert graphData is not None
    assert start <= len(graphData)
    assert end <=  len(graphData)

    frontier = []
    frontier.append(start)

    visited = []
    visited.append(start)

    parents = {}

    while frontier:
        #Get the next element in the queue
        currentIndex = frontier.pop()
        #Mark the next element as visited
        if currentIndex not in visited:
            visited.append(currentIndex)

        #Get neighbors of the current cell (passageways)
        neighbors = graphData[currentIndex][1]

        #Add neighbors to the queue
        for i in range(len(neighbors)):
            neighbor = neighbors[i]

            # see if we've visited this cell
            if neighbor not in visited:
                visited.append(neighbor)
                # add current as the neighbor's parent
                parents[neighbor] = currentIndex
                # add the neighbor to the queue
                frontier.append(neighbor)
        #Target found?
        if (currentIndex == end):
            break

    #retrace path
    path = []
    currentIndex = end
    while currentIndex != start:
        path.insert(0, currentIndex)
        currentIndex = parents[currentIndex]
    assert path is not None
    return path

def get_bfs_path():
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    path = bfs_path_creation(0, target_node)
    graphData = graph_data.graph_data[global_game_data.current_graph_index]
    secondPath = bfs_path_creation(target_node, len(graphData) - 1)
    path = path + secondPath
    assert target_node in path
    assert len(graphData) - 1 in path
    for i in range (0, len(path) - 2):
        assert path[i+1] in graphData[path[i]][1], f"Path did not find {path[i+1]} in {graphData[path[i]][1]}"
    return path

def bfs_path_creation(start, end):
    graphData = graph_data.graph_data[global_game_data.current_graph_index]
    assert graphData is not None
    assert start <= len(graphData)
    assert end <=  len(graphData)

    frontier = []
    frontier.append(start)

    visited = []
    visited.append(start)

    parents = {}

    while frontier:
        #Get the next element in the queue
        currentIndex = frontier.pop(0)
        #Mark the next element as visited
        if currentIndex not in visited:
            visited.append(currentIndex)

        #Get neighbors of the current cell (passageways)
        neighbors = graphData[currentIndex][1]

        #Add neighbors to the queue
        for i in range(len(neighbors)):
            neighbor = neighbors[i]

            # see if we've visited this cell
            if neighbor not in visited:
                visited.append(neighbor)
                # add current as the neighbor's parent
                parents[neighbor] = currentIndex
                # add the neighbor to the queue
                frontier.append(neighbor)
        #Target found?
        if (currentIndex == end):
            break

    #retrace path
    path = []
    currentIndex = end
    while currentIndex != start:
        path.insert(0, currentIndex)
        currentIndex = parents[currentIndex]
    assert path is not None
    return path



def get_dijkstra_path():
    return [1,2]

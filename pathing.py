import graph_data
import global_game_data
import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


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
    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]

import graph_data
import global_game_data
import random
import heapq as heap
import math
import f_w

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    #global_game_data.graph_paths.append(get_test_path())
    #global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    #global_game_data.graph_paths.append(get_dijkstra_path())
    global_game_data.graph_paths.append(get_f_w_path())
    global_game_data.graph_paths.append(get_a_star_path())


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
    graphData = graph_data.graph_data[global_game_data.current_graph_index]

    #First run from start to target
    path = dfs_path_creation(0, target_node)

    #Second run from target to end (starts over)
    secondPath = dfs_path_creation(target_node, len(graphData) - 1)
    path = path + secondPath
    assert target_node in path
    assert len(graphData) - 1 in path
    #Checks that there are connections between every node it wants to take
    for i in range (0, len(path) - 2):
        assert path[i+1] in graphData[path[i]][1], f"Path did not find {path[i+1]} in {graphData[path[i]][1]}"
    return path

def dfs_path_creation(start, end):
    graphData = graph_data.graph_data[global_game_data.current_graph_index]
    assert graphData is not None
    assert start <= len(graphData)
    assert end <=  len(graphData)
    #Graph data works

    frontier = []
    frontier.append(start)

    visited = []
    visited.append(start)

    parents = {}

    while frontier:
        #Pop from end
        currentIndex = frontier.pop()
        #Mark as visited if it hasn't been seen yet
        if currentIndex not in visited:
            visited.append(currentIndex)

        neighbors = graphData[currentIndex][1]
        #Deal with neighbors
        for i in range(len(neighbors)):
            neighbor = neighbors[i]

            #See if neighbors have been seen yet
            if neighbor not in visited:
                visited.append(neighbor)
                #Add the current node as the parent of this neighbor
                parents[neighbor] = currentIndex
                #Add neighbor to queue for later
                frontier.append(neighbor)
        #Target found?
        if (currentIndex == end):
            break

    #Retrace the path and record from parents
    path = []
    currentIndex = end
    while currentIndex != start:
        path.insert(0, currentIndex)
        currentIndex = parents[currentIndex]
    assert path is not None
    return path

def get_bfs_path():
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    graphData = graph_data.graph_data[global_game_data.current_graph_index]

    
    #First run from start to target
    path = bfs_path_creation(0, target_node)

    #Second run from target to end (starts over)
    secondPath = bfs_path_creation(target_node, len(graphData) - 1)
    path = path + secondPath
    assert target_node in path
    assert len(graphData) - 1 in path

    #Checks that there are connections between each node it wants to follow
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
        #Pop from top
        currentIndex = frontier.pop(0)
        #Mark as visited if not yet seen
        if currentIndex not in visited:
            visited.append(currentIndex)

        neighbors = graphData[currentIndex][1]
        #Deal with all neighbors
        for i in range(len(neighbors)):
            neighbor = neighbors[i]

            #If neighbor hasn't been seen yet
            if neighbor not in visited:
                visited.append(neighbor)
                #Add current node as this neighbor's parent
                parents[neighbor] = currentIndex
                #Add neighbor to pile
                frontier.append(neighbor)
        #Target found?
        if (currentIndex == end):
            break

    #Retrace path using parents
    path = []
    currentIndex = end
    while currentIndex != start:
        path.insert(0, currentIndex)
        currentIndex = parents[currentIndex]
    assert path is not None
    return path



def get_dijkstra_path():
    graphData = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]

    #Path start -> target
    path = dijkstras_between_two_nodes(graphData, 0, target_node, False)

    #Path target -> end
    path_2 = dijkstras_between_two_nodes(graphData, target_node, len(graphData) - 1, False)
    path_2.remove(target_node) #remove duplicate
    path += path_2

    assert path[0] == 0, 'Path does not begin at 0'
    assert path[-1] == len(graphData) - 1, 'Path does not end at end node'
    for i in range(len(path) - 2):
        assert path[i] in graphData[path[i+1]][1], f'{path[i]} not in of {graphData[path[i+1]][1]}'

    return path

def dijkstras_between_two_nodes(graph, start_index, end_index, a_star_on):
    frontier = []
    heap.heappush(frontier, (0, start_index, None, 0)) #weight, node, parent node this weight is from, actual distance
    parents = {}
    visited = set()
    for i in range(0, len(graph)):
        heap.heappush(frontier, (math.inf, i, None, math.inf)) #weight, node, parent node this weight is from, actual distance
        parents[i] = (math.inf, None) #Distance, parent
    parents[0] = (0, None) #Distance, parent


    while frontier:
        current_weight, current_node, parent_node, current_distance = heap.heappop(frontier)

        #We already popped this node once with a shorter distance, we don't need to do it again
        if current_node in visited:
            continue
        
        visited.add(current_node)
        if parents[current_node][0] > current_distance: #Reassign parent if the node we came from is better
            parents[current_node] = (current_distance, parent_node)
        
        neighbors = graph[current_node][1]
        for neighbor in neighbors:
            if neighbor not in visited: 
                new_distance = current_distance + math.sqrt(math.pow(graph[current_node][0][0] - graph[neighbor][0][0],2) + math.pow(graph[current_node][0][1] - graph[neighbor][0][1],2)) #Euclidian distance
                new_weight = new_distance
                #Only activates with A* heuristic
                if a_star_on:
                    new_weight = new_distance + math.sqrt(math.pow(graph[end_index][0][0] - graph[neighbor][0][0],2) + math.pow(graph[end_index][0][1] - graph[neighbor][0][1],2)) #Euclidian distance
                if new_distance < parents[neighbor][0]:
                    parents[neighbor] = (new_distance, current_node) #Assign parents now
                    heap.heappush(frontier, (new_weight, neighbor, current_node, new_distance)) #Stack on new heap
                    #Heap will keep the lowest weights up front, so as frontier needs emptying, stuff will need to actually be computed less and less
    
    path = []
    #Build path in reverse
    path.append(end_index)
    parent = parents[end_index][1]
    #Trace back parents
    while parent is not None:
        path.append(parent)
        parent = parents[parent][1]
    path.reverse()
    return path

def get_a_star_path():
    graphData = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]

    #Path start -> target, with A* activated
    path = dijkstras_between_two_nodes(graphData, 0, target_node, True)

    #Path target -> end, with A* activated
    path_2 = dijkstras_between_two_nodes(graphData, target_node, len(graphData) - 1, True)
    path_2.remove(target_node)
    path += path_2

    assert path[0] == 0, 'Path does not begin at 0'
    assert path[-1] == len(graphData) - 1, 'Path does not end at end node'
    for i in range(len(path) - 2):
        assert path[i] in graphData[path[i+1]][1], f'{path[i]} not in of {graphData[path[i+1]][1]}'

    return path

def get_f_w_path():
    graphData = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]

    _, parents = f_w.floyd_warshall(graphData)
    path = f_w.floyd_warshall_path(parents, 0, target_node)
    path.remove(target_node)
    path += f_w.floyd_warshall_path(parents, target_node, len(graphData) - 1)
    return path
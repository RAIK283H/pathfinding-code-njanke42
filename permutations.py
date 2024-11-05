import math

def get_permutations(start, end):
    assert start < end
    #Initial setup
    current_permutation = list(range(start, end))
    directions = []
    for i in range(len(current_permutation)):
        directions.append(-1)
    permutations_list = []
    permutations_list.append(current_permutation[:])
    
    #Generate all permutations
    largest_mobile_index = get_largest_mobile_index(current_permutation, directions)

    while largest_mobile_index != -1:
        temp_value = current_permutation[largest_mobile_index]
        temp_direction = directions[largest_mobile_index]
        if directions[largest_mobile_index] == -1: #move left
            current_permutation[largest_mobile_index] = current_permutation[largest_mobile_index - 1]
            current_permutation[largest_mobile_index - 1] = temp_value
            directions[largest_mobile_index] = directions[largest_mobile_index - 1]
            directions[largest_mobile_index - 1] = temp_direction
        else: #move right
            current_permutation[largest_mobile_index] = current_permutation[largest_mobile_index + 1]
            current_permutation[largest_mobile_index + 1] = temp_value
            directions[largest_mobile_index] = directions[largest_mobile_index + 1]
            directions[largest_mobile_index + 1] = temp_direction
        
        #flip larger values directions
        for i in range(len(current_permutation)):
            if current_permutation[i] > temp_value:
                directions[i] = -directions[i]
        permutations_list.append(current_permutation[:])
        largest_mobile_index = get_largest_mobile_index(current_permutation, directions) #reassign mobile index

    assert len(permutations_list) == math.factorial(end-start)
    return permutations_list
    


def get_largest_mobile_index(permutation, directions):
    assert len(permutation) == len(directions)

    #start at impossible
    largest_mobile_index = -1
    largest_mobile_number = -1

    for i in range(len(permutation)):
        if directions[i] == -1 and i > 0 and permutation[i] > permutation[i - 1]: #Looking left
            if permutation[i] > largest_mobile_number:
                largest_mobile_number = permutation[i]
                largest_mobile_index = i
        elif directions[i] == 1 and i < len(permutation) - 1 and permutation[i] > permutation[i + 1]: #Looking right
            if permutation[i] > largest_mobile_number:
                largest_mobile_number = permutation[i]
                largest_mobile_index = i
    return largest_mobile_index

def check_hamiltonian_cycles(graph):
    assert graph is not None
    assert len(graph) > 2
    permutations = get_permutations(1, len(graph) - 1) #All possible permutations for length
    working_permutations = [] #Will store working cycles
    if permutations is None:
        return None
    for perm in permutations:
        permutation_working = True
        #Check each one actually connected to next
        for i in range(len(perm) - 1):
            if perm[i] not in graph[perm[i+1]][1]:
                permutation_working = False
                break
        #Check it loops back right
        if perm[-1] not in graph[perm[0]][1]:
            permutation_working = False
        #IT PASSED
        if permutation_working:
            perm.append(perm[0]) #Append end on
            working_permutations.append(perm[:])
    if len(working_permutations) == 0:
        return None
    return working_permutations
        

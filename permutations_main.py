import graph_data
import permutations

if __name__ == '__main__':
    graphs = [0,1,4,7] #These are just the ones that run in reasonable time
    for item in graphs:
        cycles = permutations.check_hamiltonian_cycles(graph_data.graph_data[item])
        if cycles is None:
            print(f"No cycles found for graph {item}")
        else:
            print(f"Cycles for graph {item}: {cycles}")
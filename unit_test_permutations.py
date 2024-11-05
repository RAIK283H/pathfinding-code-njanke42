import math
import unittest
import permutations
import graph_data
import global_game_data

class TestPermutations(unittest.TestCase):
    def test_get_permutations_works_starting_from_zero(self):
        perms = permutations.get_permutations(0,3)

        expected_perms = [[0,1,2],[0,2,1],[1,2,0],[1,0,2],[2,1,0],[2,0,1]]

        self.assertEqual(len(perms), 6)
        for item in expected_perms:
            self.assertTrue(item in perms)
    
    def test_get_permutations_works_starting_from_not_zero(self):
        perms = permutations.get_permutations(2,6)

        expected_perms = [[2, 3, 4, 5], [2, 3, 5, 4], [2, 4, 3, 5], [2, 4, 5, 3], [2, 5, 3, 4], [2, 5, 4, 3], [3, 2, 4, 5], [3, 2, 5, 4], [3, 4, 2, 5], [3, 4, 5, 2], [3, 5, 2, 4], [3, 5, 4, 2], [4, 2, 3, 5], [4, 2, 5, 3], [4, 3, 2, 5], [4, 3, 5, 2], [4, 5, 2, 3], [4, 5, 3, 2], [5, 2, 3, 4], [5, 2, 4, 3], [5, 3, 2, 4], [5, 3, 4, 2], [5, 4, 2, 3], [5, 4, 3, 2]]

        self.assertEqual(len(perms), 24)
        for item in expected_perms:
            self.assertTrue(item in perms)

class TestHamiltonianCycles(unittest.TestCase):
    def test_graph_one_cycle(self):
        graph_data.graph_data[0] = [
            [(0,0), [1,2]],
            [(0,0), [0,2]],
            [(0,0), [0,1]],
        ]

        cycles = permutations.check_hamiltonian_cycles(graph=graph_data.graph_data[0])
        self.assertEqual(len(cycles), 0)


    def test_graph_two_cycles(self):


        # 3 - 2
        # |   |
        # 0 - 1
        graph_data.graph_data[0] = [
            [(0,0), [1,3]], #0
            [(0,0), [0,2]], #1
            [(0,0), [3,1]], #2
            [(0,0), [0,2]], #3
        ]

        cycles = permutations.check_hamiltonian_cycles(graph=graph_data.graph_data[0])
        self.assertEqual(len(cycles), 2)

        expected_cycles = [[1,2,1], [2,1,2]]
        for cycle in cycles:
            self.assertTrue(cycle in expected_cycles)
    
    def test_graph_six_cycles(self):
        #        3
        #      /   \
        # 0 - 1  -  2 - 4
        graph_data.graph_data[0] = [
            [(0,0), [1]], #0
            [(0,0), [0,2,3]], #1
            [(0,0), [3,1,4]], #2
            [(0,0), [1,2]], #3
            [(0,0), [2]], #4
        ]

        cycles = permutations.check_hamiltonian_cycles(graph=graph_data.graph_data[0])
        self.assertEqual(len(cycles), 6)

        expected_cycles = [[1,2,3,1], [1,3,2,1], [2,3,1,2], [2,1,3,2], [3,1,2,3], [3,2,1,3],]
        for cycle in cycles:
            self.assertTrue(cycle in expected_cycles)
    
    def test_no_cycles_on_chain(self):
        # 0 - 1 - 2 - 3 - 4
        graph_data.graph_data[0] = [
            [(0,0), [1]], #0
            [(0,0), [0,2]], #1
            [(0,0), [3,1]], #2
            [(0,0), [2,4]], #3
            [(0,0), [3]], #4
        ]
        cycles = permutations.check_hamiltonian_cycles(graph=graph_data.graph_data[0])
        self.assertEqual(len(cycles), 0)


if __name__ == '__main__':
    unittest.main()
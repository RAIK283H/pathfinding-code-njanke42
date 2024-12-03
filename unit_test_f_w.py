import math
import unittest
import f_w
import graph_data
import global_game_data

class TestDijkstrasPathFinding(unittest.TestCase):

    def test_f_w_edge(self):
        graph = [
        [(900, 45), [3]], #0, now 0
        [(420, 420), [2]], #13, now 1
        [(560, 420), [3,1]], #15, now 2
        [(630, 210), [0,2]], #17, now 3
        ]
        _, parents = f_w.floyd_warshall(graph)
        path = f_w.floyd_warshall_path(parents, 0, 3)
        expected_path = [0,1,2,3]
        self.assertEqual(path, expected_path, f"{path} is not {expected_path}")

    #test to check returning a working graph
    def test_hits_target_and_end(self):

        #Graph Structure
        #  0 - 1 - 2 - 3
        graph = [
            [(0, 0), [1]], #0
            [(10, 0), [0,2]], #1
            [(20, 0), [1,3]], #2
            [(30, 0), [2]], #3
        ]
        _, parents = f_w.floyd_warshall(graph)
        path = f_w.floyd_warshall_path(parents, 0, 3)
        expected_path = [0,1,2,3]
        self.assertEqual(path, expected_path, f"{path} is not {expected_path}")

    #test to check that dijkstras care about distance over nodes visited
    def test_f_w_cares_about_distance(self):
        #Graph Structure
        #          1
        #         / \
        #        /   \
        #       /     \
        #      /       \
        #     /         \
        #    /           \
        #   /             \
        #  0 - 2 - 3 - 4 - 5
        graph = [
            [(0, 0), [1,2]], #0
            [(40, 500), [0,5]], #1
            [(20, 0), [0,3]], #2
            [(40, 0), [2,4]], #3
            [(60, 0), [3,5]], #4
            [(80, 0), [4,1]], #5
        ]
        _, parents = f_w.floyd_warshall(graph)
        path = f_w.floyd_warshall_path(parents, 0, 5)
        expected_path = [0,2,3,4,5]
        self.assertEqual(path, expected_path, f"{path} is not {expected_path}")

if __name__ == '__main__':
    unittest.main()
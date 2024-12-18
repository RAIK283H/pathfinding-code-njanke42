import math
import unittest
import pathing
import graph_data
import global_game_data


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

class TestRandomPathFinding(unittest.TestCase):

    #test on graph that might allow for failure
    def test_hits_target_and_end(self):

        #Graph Structure:
        #         4
        #         |
        #         3
        #         |
        # 0 - 1 - 2 - 5 - 6
        graph_data.graph_data[0] = [
            [(0, 0), [1]], #0
            [(0, 0), [0,2]], #1
            [(0, 0), [1,3,5]], #2
            [(0, 0), [2,4]], #3, extends to target node
            [(0, 0), [3]], #4, target node
            [(0, 0), [2,6]], #5
            [(0, 0), [5]], #6
        ]
        global_game_data.current_graph_index = 0
        global_game_data.target_node.append(4)
        path = pathing.get_random_path()
        self.assertIn(2, path) #check it found target
        self.assertEqual(path[len(path) - 1], 6) #check it ends on end

class TestBFSPathFinding(unittest.TestCase):
    #test to check returning a working graph
    def test_hits_target_and_end(self):

        #Graph Structure:
        #         4
        #         |
        #         3
        #         |
        # 0 - 1 - 2 - 5 - 6
        graph_data.graph_data[0] = [
            [(0, 0), [1]], #0
            [(0, 0), [0,2]], #1
            [(0, 0), [1,3,5]], #2
            [(0, 0), [2,4]], #3, extends to target node
            [(0, 0), [3]], #4, target node
            [(0, 0), [2,6]], #5
            [(0, 0), [5]], #6
        ]
        global_game_data.current_graph_index = 0
        global_game_data.target_node = []
        global_game_data.target_node.append(4)
        path = pathing.get_bfs_path()
        self.assertIn(2, path) #check it found target
        self.assertEqual(path[len(path) - 1], 6) #check it ends on end

    def test_actually_bfs(self):
        #Graph Structure
        #
        #
        #         2 - - - - - - - 7
        #         |               |
        #     0 - 1 - 3 - 4 - 5 - 6
        graph_data.graph_data[0] = [
            [(0, 0), [1]], #0
            [(0, 0), [0,2,3]], #1
            [(0, 0), [1,7]], #2
            [(0, 0), [1,4]], #3, extends to target node
            [(0, 0), [3,5]], #4, target node
            [(0, 0), [4,6]], #5
            [(0, 0), [5,7]], #6
            [(0, 0), [2,6]], #7
        ]
        global_game_data.current_graph_index = 0
        global_game_data.target_node = []
        global_game_data.target_node.append(1)
        path = pathing.get_bfs_path()
        self.assertIn(1, path) #check it found target
        expectedPath = [1,2,7]
        self.assertEqual(path, expectedPath) #check it actually did bfs

class TestDFSPathFinding(unittest.TestCase):
    #test to check returning a working graph
    def test_hits_target_and_end(self):

        #Graph Structure
        #      2 - - - - - - - 7
        #      |               |
        #  0 - 1 - 3 - 4 - 5 - 6
        #BFS will find 1,2,7. DFS will not
        graph_data.graph_data[0] = [
            [(0, 0), [1]], #0
            [(0, 0), [0,2]], #1
            [(0, 0), [1,3,5]], #2
            [(0, 0), [2,4]], #3, extends to target node
            [(0, 0), [3]], #4, target node
            [(0, 0), [2,6]], #5
            [(0, 0), [5]], #6
        ]
        global_game_data.current_graph_index = 0
        global_game_data.target_node = []
        global_game_data.target_node.append(4)
        path = pathing.get_dfs_path()
        self.assertIn(2, path) #check it found target
        self.assertEqual(path[len(path) - 1], 6) #check it ends on end

    def test_actually_bfs(self):
        #Graph Structure
        #      2 - - - - - - - 7
        #      |               |
        #  0 - 1 - 3 - 4 - 5 - 6
        #BFS will find 1,2,7. DFS will not
        graph_data.graph_data[0] = [
            [(0, 0), [1]], #0
            [(0, 0), [0,2,3]], #1
            [(0, 0), [1,7]], #2
            [(0, 0), [1,4]], #3, extends to target node
            [(0, 0), [3,5]], #4, target node
            [(0, 0), [4,6]], #5
            [(0, 0), [5,7]], #6
            [(0, 0), [2,6]], #7
        ]
        global_game_data.current_graph_index = 0
        global_game_data.target_node = []
        global_game_data.target_node.append(1)
        path = pathing.get_dfs_path()
        self.assertIn(1, path) #check it found target
        expectedPath = [1,3,4,5,6,7]
        self.assertEqual(path, expectedPath) #check it actually did bfs

class TestDijkstrasPathFinding(unittest.TestCase):
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
        path = pathing.dijkstras_between_two_nodes(graph, 0, 3, False)
        expected_path = [0,1,2,3]
        self.assertEqual(path, expected_path, f"{path} is not {expected_path}")

    #test to check that dijkstras care about distance over nodes visited
    def test_dijkstras_cares_about_distance(self):
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
        path = pathing.dijkstras_between_two_nodes(graph, 0, 5, False)
        expected_path = [0,2,3,4,5]
        self.assertEqual(path, expected_path, f"{path} is not {expected_path}")
    
    #This tests the actual path making algorithm used by the program (uses target)
    def test_dijkstras_path_making_works(self):
        #Graph Structure
        #          1
        #         / \
        #        /   \
        #       /     \
        #      /       \
        #     /         \
        #    /           \
        #   /             \
        #  0 - 2 - 3 - 4 - 5 - 6
        graph_data.graph_data[0] = [
            [(0, 0), [1,2]], #0
            [(40, 500), [0,5]], #1
            [(20, 0), [0,3]], #2
            [(40, 0), [2,4]], #3
            [(60, 0), [3,5]], #4
            [(80, 0), [4,1,6]], #5
            [(100, 0), [5]], #6
        ]
        global_game_data.current_graph_index = 0
        global_game_data.target_node = []
        global_game_data.target_node.append(5)
        path = pathing.get_dijkstra_path()
        self.assertIn(5, path) #check it found target
        expectedPath = [0,2,3,4,5,6]
        self.assertEqual(path, expectedPath) #check it actually did bfs
    
    #Tests A*
    def test_a_star(self):
        #Graph Structure
        #          1
        #         / \
        #        /   \
        #       /     \
        #      /       \
        #     /         \
        #    /           \
        #   /             \
        #  0 - 2 - 3 - 4 - 5 - 6
        graph_data.graph_data[0] = [
            [(0, 0), [1,2]], #0
            [(40, 500), [0,5]], #1
            [(20, 0), [0,3]], #2
            [(40, 0), [2,4]], #3
            [(60, 0), [3,5]], #4
            [(80, 0), [4,1,6]], #5
            [(100, 0), [5]], #6
        ]
        global_game_data.current_graph_index = 0
        global_game_data.target_node = []
        global_game_data.target_node.append(5)
        path = pathing.get_a_star_path()
        self.assertIn(5, path) #check it found target
        expectedPath = [0,2,3,4,5,6]
        self.assertEqual(path, expectedPath) #check it actually did bfs

if __name__ == '__main__':
    unittest.main()

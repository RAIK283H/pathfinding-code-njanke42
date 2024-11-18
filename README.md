# Pathfinding Starter Code

Random Pathfinding Algorithm:
    The algorithm shall move the player randomly between connected nodes. When a player reaches a node, it will select a random node to move to next from its current node's neighbors. This list includes the node the player arrived from, which makes the pathing truly random. As a result, this algorithm is incredibly bad. This process of selecting new nodes and moving to them will repeat until the player has both visited the target and arrived at the end. The target can be visited at any time, but the end must be the final node to be visited. The algorithm will keep track of all visited nodes in a list for the player to follow.

Statistics Page Addition:
    This new addition to the statistics page will track the number of nodes the player visits. It will update based on information from the player. The player object will be updated to track number of nodes visited. If a player visits a node multiple times, it will count each of those visits seperately. The nodes will be tracked in real time.

New Graph:
    Another graph was added with 27 nodes. It is designed to throw off the random path algorithm by having long sections of paths it can go down, without much interconnectedness that could give it an advantage. It must go down this long path to find the target and then return to find the exit. Initially it was designed so only the beginning was connected to the exit, but this made path calculation unreasonably long in most circumstances, so additional connections were added.


HOMEWORK 6 EXTRA CREDIT
I implemented a heapqueue to implement my priority queue. To ensure everything worked, I popped lowest weight values first and had a dictionary of nodes I had already visited (completed). If I popped a node that I already completed, I discarded it without any computation, which was my way of updating priorities. Therefore, the benefits of priority queue were maintained.

I also implemented the A* algorithm using the distance from the node to the desired end as the heuristic. This is applicable because it will always underestimate or equal the true distance. I made sure to keep the weight value and the true distance value seperate so Dijkstras still functions.
'''
graph_data[a] = gives you graph at index a
graph_data[a][0] = start node of graph a
graph_data[a][length-1] = exit node of graph a
graph_data[a][b][0] = x-y coordinates as tuple of point b in graph a
graph_data[a][b][1] = adjacency list of point b in graph a

Only the start and exit nodes are dead ends (all other nodes have degree >= 2)
'''


graph_data = [
    #0
    [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1]]
    ],
    #1
    [
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2]]
    ],
    #2
    [
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
    ],
    #3
    [
        [(0, 0), [1, 4]],
        [(0, 100), [0, 2, 5]],
        [(0, 200), [1, 3, 6]],
        [(0, 300), [2, 7]],
        [(100, 0), [5, 0, 8]],
        [(100, 100), [4, 6, 1, 9]],
        [(100, 200), [5, 7, 2, 10]],
        [(100, 300), [6, 3, 11]],
        [(200, 0), [9, 4, 12]],
        [(200, 100), [8, 10, 5, 13]],
        [(200, 200), [9, 11, 6, 14]],
        [(200, 300), [10, 7, 15]],
        [(300, 0), [13, 8]],
        [(300, 100), [12, 14, 9]],
        [(300, 200), [13, 15, 10]],
        [(300, 300), [14,11]],
    ],
    #4
    [
        [(45, 45), [1]], #0
        [(100, 245), [0, 2, 4]], #1
        [(200, 245), [1, 3, 5]], #2
        [(300, 145), [2, 6]], #3
        [(100, 345), [1, 5, 7]], #4
        [(200, 345), [2, 4, 6, 8]], #5
        [(300, 345), [3, 5, 9]], #6
        [(100, 545), [4, 8]], #7
        [(200, 445), [5, 7, 9]], #8
        [(300, 445), [6, 8, 10]], #9
        [(1200, 700), [9]] #10
    ],
    #5
    [
        [(45, 45), [1]],
        [(100, 245), [14, 0, 2]],
        [(200, 245), [1, 5, 3]],
        [(300, 245), [2, 6, 10, 11, 12]],
        [(500, 345), [13, 6, 9]],
        [(200, 345), [14, 2, 6, 8]],
        [(300, 345), [9, 5, 4, 3]],
        [(100, 545), [8, 14]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [4, 6, 8, 15]],
        [(200, 145), [3, 11]],
        [(300, 145), [3, 10, 12]],
        [(400, 145), [3, 11, 13]],
        [(500, 145), [4, 12]],
        [(100, 345), [1, 7, 5]],
        [(1200, 700), [9]],
    ],
    #6
    [
        [(0,0), [1, 26]], #0
        [(0, -45), [0, 2]], #1
        [(0, -90), [1, 3]], #2
        [(0, -135), [2, 4]], #3
        [(0, -180), [3, 5]], #4
        [(0, -225), [4, 6]], #5
        [(45, -225), [5, 7]], #6
        [(45, -180), [6, 8]], #7
        [(45, -135), [7, 9]], #8
        [(45, -90), [8, 10]], #9
        [(45, -45), [9, 11, 26]], #10
        [(90, -45), [10, 12, 26]], #11
        [(90, -90), [11, 13]], #12
        [(90, -135), [12, 14]], #13
        [(90, -180), [13, 15]], #14
        [(90, -225), [14, 16]], #15
        [(135, -225), [15, 17]], #16
        [(135, -180), [16, 18]], #17
        [(135, -135), [17, 19]], #18
        [(135, -90), [18, 20]], #19
        [(135, -45), [19, 21, 26]], #20
        [(180, -45), [20, 22, 26]], #21
        [(180, -90), [21, 23]], #22
        [(180, -135), [22, 24]], #23
        [(180, -180), [23, 25]], #24
        [(180, -225), [24]], #25
        [(45,0), [0, 10, 11, 20, 21]] #26
    ],
    # #7
    # [
    #     [(0,0), [1]],
    #     [(0,0), [0,2]],
    #     [(0,0), [1,3,4]],
    #     [(0,0), [1,2]],
    #     [(0,0), [2]]
    # ]
]

test_path = [
    [1, 2],
    [1, 2, 3],
    [22, 3, 11, 17, 18, 23],
    [1, 5, 6, 10, 11, 15],
    [1, 2, 5, 8, 9, 10],
    [1, 14, 5, 6, 9, 15],
    [26],
]

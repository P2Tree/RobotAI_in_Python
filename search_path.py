
# Grid format:
# 0 = Navigable space
# 1 = Occupied space
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]] # this is the same as image grid

init = [0, 0]   # starting position
goal = [len(grid)-1, len(grid[0])-1]    # goal position
delta = [[-1, 0],#go up
        [0, -1],#go left
        [1, 0],#go down
        [0, 1]]#go right

delta_name = ['^', '<', 'v', '>']

cost = 1 # each move consts

def search():
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    count = 0
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed = [[0] * len(grid[0]) for i in grid]
    closed[init[0]][init[1]] = 1 # set starting cell to 1
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    open = [[g, x, y]]

    found = False # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        
        if len(open) == 0:
            resign = True
            return "fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] = count
            count += 1

            print "next step", [g, x, y]
        if x == goal[0] and y == goal[1]:
            found = True
            #for i in range(len(expand)):
            #    print expand[i]

            #return "result", [g, x, y]
        else:
            for i in range(len(delta)):
                # in this case, [x, y] represents the "from" state, but [x2, y2] represents the "next" state
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                        g2 = g + cost
                        open.append([g2, x2, y2])
                        closed[x2][y2] = 1
                        action[x2][y2] = i
    # 
    policy = [[' '] * len(grid[0]) for i in grid]
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    while x!= init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2
    for i in range(len(policy)):
        print policy[i]


print "Grid:"
for i in range(len(grid)):
    print grid[i]
print "------"
#print "A* algorithm to find the path in grid is:([g_value, x_set, y_set])"
#print search()

search()

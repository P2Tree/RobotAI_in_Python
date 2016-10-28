
# Grid format:
# 0 = Navigable space
# 1 = Occupied space
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]] # this is the same as image grid

init = [0, 0]   # starting position
goal = [len(grid)-1, len(grid[0])-1]    # goal position
delta = [[-1, 0],#go up
        [0, -1],#go left
        [1, 0],#go down
        [0, 1]]#go right

cost = 1 # each move consts

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed = [[0] * len(grid[0]) for i in grid]

    closed[init[0]][init[1]] = 1 # set starting cell to 1

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
            print "next step", [g, x, y]
        if x == goal[0] and y == goal[1]:
            found = True
            return "result", [g, x, y]
        else:
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                        g2 = g + cost
                        open.append([g2, x2, y2])
                        closed[x2][y2] = 1


print "Grid:"
for i in range(len(grid)):
    print grid[i]

print "A* algorithm to find the path in grid is:([g_value, x_set, y_set])"
print search()

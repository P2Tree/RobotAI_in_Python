
# Grid format:
# 0 = Navigable space
# 1 = Occupied space
grid = [[0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0]] # this is the same as image grid

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]   # starting position
goal = [len(grid)-1, len(grid[0])-1]    # goal position
delta = [[-1, 0],#go up
        [0, -1],#go left
        [1, 0],#go down
        [0, 1]]#go right

delta_name = ['^', '<', 'V', '>']

cost = 1 # each move consts

def search():
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1 # set starting cell to 1

    x = init[0]
    y = init[1]
    g = 0
    count = 0
    h = heuristic[x][y]
    f = g + h
    open = [[f, g, h, x, y]]

    found = False # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            # checkout the minimum open[x][0] in the open list
            next = open.pop()
            x = next[3]
            y = next[4]
            g = next[1]
            h = next[2]
            f = next[0]
            expand[x][y] = count
            count += 1
            print "step", [f, g, h, x, y]
        if x == goal[0] and y == goal[1]:
            found = True

        else:
            for i in range(len(delta)):
                # use [x, y] is the minimum open[x][0] in open list
                # so in this case, only the minimum f point in the 
                # open list can be expand here
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                        g2 = g + cost
                        h2 = heuristic[x2][y2]
                        f2 = g2 + h2
                        print "expand:", [x2, y2]
                        open.append([f2, g2, h2, x2, y2])
                        closed[x2][y2] = 1

    for i in range(len(expand)):
        print expand[i]
    return expand

print "Grid:"
for i in range(len(grid)):
    print grid[i]

print "----- result -----"
print " f, g, h, x, y"
search()

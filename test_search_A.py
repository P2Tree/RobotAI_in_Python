
# Grid format:
# 0 = Navigable space
# 1 = Occupied space
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]] # this is the same as image grid

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

cost = 1 # each move consts

def search():
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    count = 0
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed = [[0] * len(grid[0]) for i in grid]
    closed[init[0]][init[1]] = 1 # set starting cell to 1

    x = init[0]
    y = init[1]
    g = 0
    f0 = heuristic[0][0] + g
    minf= f0
    open = [[g, f0, x, y]]

    found = False # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        minlist = []
        if len(open) == 0:
            resign = True
            return "fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[2]
            y = next[3]
            g = next[0]
            f = next[1]
            expand[x][y] = count
            count += 1
            print "step", [g, f, x, y]
        if x == goal[0] and y == goal[1]:
            found = True
            for i in range(len(expand)):
                print expand[i]

            return "result", [g, f, x, y]
        else:
            check = []
            print "check which point to expand:"
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                print "check:", [x2, y2]
                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0 and f == minf:
                        print [x2, y2], "is right to expand"
                        g2 = g + cost
                        f2 = heuristic[x2][y2] + g2
                        minlist.append(f2)
                        #open.append([g2, f2, x2, y2])
                        closed[x2][y2] = 1
                        print [x2, y2], "f2=", f2
                        print "min of minlist:", min(minlist)
                        check.append([g2, f2, x2, y2])
            print "check expand done"
            print "check min f_value:"
            for i in range(len(check)):
                checkset = check.pop()
                cx = checkset[2]
                cy = checkset[3]
                cf = checkset[1]
                cg = checkset[0]
                print "check:", [cx, cy]
                if cf > min(minlist):
                    closed[cx][cy] = 1
                    print [cx, cy], "closed"
                elif cf == min(minlist):
                    open.append([cg, cf, cx, cy])
                    print [cx, cy], "add to open list"
            if len(minlist) > 0:
                print "minlist:", minlist
                minf = min(minlist)
                print "minf:", minf
        print "-----"


print "Grid:"
for i in range(len(grid)):
    print grid[i]

print "A* algorithm to find the path in grid is:([g_value, x_set, y_set])"
print search()

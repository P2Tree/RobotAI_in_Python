# This piece of python script is uesd to find the optimum street cross policy in a simulate map(grid)
# run the code it will show you the map and the optimum policy
# car have three arguments: x-set y-set orientation

# map: 1 is obstacles and 0 is streets
grid = [[0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1]]

# goal:
goal = [4, 1] # final position

# start:
init = [4, 3, 0] # first 2 elements are coordinate, third is direction

# cost:
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# there are four motion direction: up left down right
# increasing the index in this array corresponds to a left turn. Decreasing is a right turn

forward = [[-1, 0], # go up
           [0, -1], # go left
           [1, 0], # go down
           [0, 1]] # go right

forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

def optimum_policy2D():
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    policy = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]]

    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    change = True
    
    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for orientation in range(4):
                    if goal[0] == x and goal[1] == y:
                        if value[orientation][x][y] > 0:
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                            change = True
                    elif grid[x][y] == 0: # do not need to consider out-of-range of [x, y] in grid
                        for i in range(3): # turn left or go forward or turn right
                            o2 = (orientation + action[i]) % 4
                            x2 = x + forward[o2][0]
                            y2 = y + forward[o2][1]
                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[o2][x2][y2] + cost[i]
                                if v2 < value[orientation][x][y]:
                                    change = True
                                    value[orientation][x][y] = v2
                                    policy[orientation][x][y] = action_name[i]
    # make 2D map from 3D matrix
    x = init[0]
    y = init[1]
    orientation = init[2]
    policy2D[x][y] = policy[orientation][x][y]
    while policy[orientation][x][y] != '*':
        if policy[orientation][x][y] == '#':
            o2 = orientation
        elif policy[orientation][x][y] == 'R':
            o2 = (orientation - 1) % 4
        elif policy[orientation][x][y] == 'L':
            o2 = (orientation + 1) % 4
        x = x + forward[o2][0]
        y = y + forward[o2][1]
        orientation = o2
        policy2D[x][y] = policy[orientation][x][y]
    return policy2D

policy2D = optimum_policy2D()

print "map: (1 is obstacles and 0 is streets)"
for i in range(len(grid)):
    print grid[i]

print "goal point is:"
print goal

print "init point is:"
print init

print "cost is:"
print cost

print "optimum policy track is:"
for i in range(len(policy2D)):
    print policy2D[i]

# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of 
# accuracy is reached. The update should be done according
# to the gradient descent qquations.

from math import *

path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1,
            tolerance = 0.000001):
    # make a deep copy of path into newpath
    newpath = [[0 for col in range(len(path[0]))]
                for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]

    change = tolerance
    while (change >= tolerance):
        change = 0
        for i in range(1, len(path)-1): # exclude the first and last point
            for j in range(len(path[0])):
                d1 = weight_data * (path[i][j] - newpath[i][j])
                d2 = weight_smooth * (newpath[i-1][j] + newpath[i+1][j] - 2 * newpath[i][j])

                change += abs(d1 + d2)
                newpath[i][j] += d1 + d2

    return newpath

newpath = smooth(path)

for i in range(len(path)):
    print '[' + ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ \
            ', '.join('%.3f'%x for x in newpath[i]) + ']'

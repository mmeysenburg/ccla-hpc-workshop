import math
import random
import sys
from timeit import default_timer as timer

def euclideanToPolar(points):
    '''
    Convert a list of Euclidean point to polar coordinates.

    parameter
    ---------
        point: list of tuples with (x, y) coordinate

    returns
    -------
        list of tuples with (theta, r) coordinate
    '''
    return [(math.atan(point[1] / point[0]), math.sqrt(point[0] ** 2 + point[1] ** 2))
        for point in points]

n = int(sys.argv[1])

elapsed = 0
for trial in range(5):
    euclideans = [(random.random(), random.random()) for i in range(n)]

    startTime = timer()
    polars = euclideanToPolar(euclideans)
    stopTime = timer()

    elapsed += (stopTime - startTime)

print('{0:d},{1:f}'.format(n, elapsed))
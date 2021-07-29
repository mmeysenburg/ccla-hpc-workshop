import math
import random
import sys
from timeit import default_timer as timer

def cartesianToPolar(point):
    '''
    Convert a Cartesian point to polar coordinates.

    parameter
    ---------
        point: tuple with (x, y) coordinate

    returns
    -------
        tuple with (theta, r) coordinate
    '''
    theta = math.atan(point[1] / point[0])
    r = math.sqrt(point[0] ** 2 + point[1] ** 2)
    return (theta, r)

n = int(sys.argv[1])

elapsed = 0
for trial in range(5):
    euclideans = [(random.random(), random.random()) for i in range(n)]

    startTime = timer()
    polars = [cartesianToPolar(p) for p in euclideans]
    stopTime = timer()

    elapsed += (stopTime - startTime)

print('{0:d},{1:f}'.format(n, elapsed / 5))
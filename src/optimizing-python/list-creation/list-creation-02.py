'''
Creating a list of appropriate size, then adding by index.
'''
from timeit import default_timer as timer
import random
import sys

n = int(sys.argv[1])

startTime = timer()
values = [0] * n
for i in range(n):
    values[i] = random.random()
stopTime = timer()

print('{0:d},{1:f}'.format(n, stopTime - startTime))

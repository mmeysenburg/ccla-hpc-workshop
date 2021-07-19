'''
Creating a list then adding by appending.
'''
from timeit import default_timer as timer
import random
import sys

n = int(sys.argv[1])

startTime = timer()
values = []
for i in range(n):
    values.append(random.random())
stopTime = timer()

print('{0:d},{1:f}'.format(n, stopTime - startTime))

'''
Create and fill a list of n random floats in [0, 1).
This version uses a list comprehension.
'''

from timeit import default_timer as timer
import random
import sys

values = []

n = int(sys.argv[1])

startTime = timer()
values = [random.random() for i in range(n)]

stopTime = timer()

print('{0:d},{1:f}'.format(n, stopTime - startTime))
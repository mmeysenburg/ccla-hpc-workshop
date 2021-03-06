'''
Create and fill a list of n random floats in [0, 1).
This version uses list comprehension to populate the list, 
accessing the random.random() method via an alias.
'''

from timeit import default_timer as timer
import random
import sys

values = []

n = int(sys.argv[1])

rand = random.random
startTime = timer()
values = [rand() for i in range(n)]
stopTime = timer()

print('{0:d},{1:f}'.format(n, stopTime - startTime))
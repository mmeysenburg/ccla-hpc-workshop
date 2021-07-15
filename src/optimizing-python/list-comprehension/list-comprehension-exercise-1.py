'''
Code to select only the even numbers from a large list.
'''
from timeit import default_timer as timer
import random

# list creation
rawValues = [random.randrange(0, 100000) for i in range(100000000)]

# loop version
evenValues = []
startTime1 = timer()
for v in rawValues:
    if v % 2 == 0:
        evenValues.append(v)
stopTime1 = timer()

# list comprehension version
evenValues = []
startTime2 = timer()
evenValues = [x for x in rawValues if x % 2 == 0]
stopTime2 = timer()

print('{0:f},{1:f}'.format(stopTime1 - startTime1, 
    stopTime2 - startTime2))

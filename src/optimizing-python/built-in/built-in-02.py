'''
Finding min / max value via built-in functions.
'''
from timeit import default_timer as timer
import random
import sys

for n in range(2000000, 100000000, 2000000):
    elapsed = 0.0
    for trial in range(5):
        values = [random.random() for i in range(n)]

        startTime = timer()
        mininum = min(values)
        maximum = max(values)
        stopTime = timer()

        elapsed += (stopTime - startTime)
    
    print('{0:d},{1:f}'.format(n, elapsed / 5))

        

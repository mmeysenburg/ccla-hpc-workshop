'''
Finding min / max value via looping.
'''
from timeit import default_timer as timer
import random
import sys

for n in range(0, 100000000, 2000000):
    elapsed = 0.0
    for trial in range(5):
        values = [random.random() for i in range(n)]

        startTime = timer()
        min = 2.0
        max = -2.0
        for v in values:
            if v < min:
                min = v
            if v > max:
                max = v 
        stopTime = timer()

        elapsed += (stopTime - startTime)
    
    print('{0:d},{1:f}'.format(n, elapsed / 5))

        

'''
Function alias exercise 2

Convert cartesian coordinates to polar.
'''

import math
import random

# create n cartesian coordinates in the unit square
n = 1_000_000
uni = random.uniform
cartesians = [(uni(-1, 1), uni(-1, 1)) for i in range(n)]

# write code here to create a new list called polars.
# the new list should contain the polar coordinate
# equivalents of each of the coors in cartesians.
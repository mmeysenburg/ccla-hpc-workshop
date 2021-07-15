import random

# create 100,000 random values in [1, 100]
rand = random.randrange
data = [rand(1, 101) for i in range(100000)]

# write code to create a list of the square roots
# of the values in data. 
# use an alias to speed up access to the function
import math
sqrt = math.sqrt
squareRoots = [sqrt(x) for x in data]

print(squareRoots)
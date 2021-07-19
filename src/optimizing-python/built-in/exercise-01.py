# Exercise 1 - summing values

from timeit import default_timer as timer
import random

# list size
n = 100000

# create randomly-populated list
values = [random.randrange(1000) for i in range(n)]

# part 1: write native Python to sum the list,
# using the accumulator pattern; store the sum
# in the variable named nativeSum
nativeStart = timer()

nativeSum = 0
# your code here
for v in values:
    nativeSum += v

nativeStop = timer()

# part 2: find sum via built-in; store the sum
# in the variable named biSum
biStart = timer()

biSum = 0
# your code here
biSum = sum(values)

biStop = timer()

print('Native time elapsed:', nativeStop - nativeStart)
print('Built-in time elapsed:', biStart - biStop)

if nativeSum == biSum:
    print('Sums are equal')
else:
    print('SUMS WERE NOT THE SAME')
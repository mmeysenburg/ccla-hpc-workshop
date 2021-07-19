import random

# seed PRNG so the same numbers happen each time
random.seed(68333)

# create 100,000 randoms in [1, 10]
data = [random.randrange(1,11) for i in range(100000)]

# view frequency of each value
for i in range(1, 11):
    freq = sum([1 for x in data if x == i])
    print('{0:3d}:\t{1:d}'.format(i, freq))
import numpy as np 
import sys

n = int(sys.argv[1])

A = np.random.randint(1, 101, size = (n, n))
B = np.random.randint(1, 101, size = (n, n))
Cn = np.zeros((n, n))

from timeit import default_timer as timer

naiveElapsed = 0
for run in range(5):
    naiveStart = timer()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Cn[i][j] += A[i][k] * B[k][j]
    naiveStop = timer()
    naiveElapsed += (naiveStop - naiveStart)

npElapsed = 0
for run in range(5):
    npStart = timer()
    Cny = np.matmul(A, B)
    npStop = timer()
    npElapsed += (npStop - npStart)

naiveElapsed /= 5
npElapsed /= 5

speedup = naiveElapsed / npElapsed

print('{0:d},{1:f},{2:f},{3:f}'.format(n, naiveElapsed, npElapsed, speedup))
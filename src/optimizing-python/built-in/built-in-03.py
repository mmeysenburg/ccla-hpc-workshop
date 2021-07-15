import numpy as np 
import sys

n = int(sys.argv[1])

A = np.random.randint(1, 101, size = (n, n))
B = np.random.randint(1, 101, size = (n, n))
Cn = np.zeros((n, n))

from timeit import default_timer as timer

naiveStart = timer()
for i in range(n):
    for j in range(n):
        for k in range(n):
            Cn[i][j] += A[i][k] * B[k][j]

naiveStop = timer()

npStart = timer()
Cny = np.matmul(A, B)
npStop = timer()

naiveElapsed = naiveStop - naiveStart
npElapsed = npStop - npStart

speedup = naiveElapsed / npElapsed

print('{0:d},{1:f},{2:f},{3:f}'.format(n, naiveElapsed, npElapsed, speedup))
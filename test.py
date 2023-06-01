from numba import jit, cuda
import numpy as np
# to measure exec time
from timeit import default_timer as timer


# normal function to run on cpu

start = timer()



def zebi():
    a = 0
    for i in range(10000000):
        a += 1
    return a


print(zebi())
print(timer()-start)

# function optimized to run on gpu




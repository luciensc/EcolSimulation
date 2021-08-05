import numpy as np
from joblib import Parallel, delayed

ra = np.array(np.arange(0,25)).reshape(5,5)

x = [(i, j) for i in range(5) for j in range(5)]

# if writing to original file: doesn't work bc shared memory problems (process makes copy of array)
# https://joblib.readthedocs.io/en/latest/parallel.html#writing-parallel-computation-results-in-shared-memory
# avoid by changing implementation:
# INVERSE PARADIGM: COMPUTE CURRENT POSITION BASED ON SUMMING UP ALL OTHER POSITIONS

def square(i, j):
    return ra[i, j]**2  # np.square(ra) (w/o return) doesn't work

rtrn = Parallel(n_jobs=2)(delayed(square)(i, j) for i in range(ra.shape[0]) for j in range(ra.shape[1]))
#[square(i) for i in range(len(ra))]
#print(ra)
print(ra)
print(np.array(rtrn).reshape(5, 5))
print("")


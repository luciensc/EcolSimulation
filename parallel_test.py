import numpy as np
from joblib import Parallel, delayed

ra = [i for i in range(10)]

def square(i):
    ra[i] = i**2

[square(i) for i in range(len(ra))]
print(ra)



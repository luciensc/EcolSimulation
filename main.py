# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from datetime import datetime as dtt
# import os
# import pickle
# import time

from grid import Grid
from run_functions import run_simulation
"""
ecological simulation

2D grid

seasonal organism
"""

LENGTH = 50  # square grid length
DISPERSAL_DECAY = 4  # exponent for decay. higher exponent -> faster decay.
N_SPAWN = 1  # how many cells on the grid are initialised with an organism
ecol_distr_types = ["random_uniform", "random_binary"]
ECOL_DISTR = ecol_distr_types[0]
BERNOULLI = False

seed_ecol = 1859  # initialisation of fitness distribution (grid.ecol)
seed_spawn = 380  # selection of initially populated cells in the grid.
# seed_sim = 42  # stochastic effects during simulation

# save = True
# gif = False  # may only be True if 'save' is True
# optional descriptor of current experiment for logging purposes
description = f"SPAWNVAR_nspawn{N_SPAWN}_seedspawn{seed_spawn}"
#"VARIANCE__decay" + str(DISPERSAL_DECAY) + "_ecol" + str(seed_ecol) + "_spawn" + str(seed_spawn)


grid = Grid(length=LENGTH, disp_decay=DISPERSAL_DECAY, ecol_distr=ECOL_DISTR, n_spawn=N_SPAWN, seed_ecol=seed_ecol,
            seed_spawn=seed_spawn)

run_simulation(grid, n_run=100, plot_freq=1, seed_sim=42, n_jobs=1, save=True, gif=False, description=description)



import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from datetime import datetime as dtt
import os
import pickle
import time

from grid import Grid
from aux_functions import *

"""
ecological simulation

2D grid

seasonal organism
"""
save = True
description = "uniform_decay4"  # optional descriptor of current experiment for logging purposes

n_run = 30
plot_freq = 5

LENGTH = 50  # square grid length
DISPERSAL_DECAY = 4  # exponent for decay. higher exponent -> faster decay.
N_SPAWN = 10  # how many cells on the grid are initialised with an organism
ecol_distr_types = ["random_uniform", "random_binary"]
ECOL_DISTR = ecol_distr_types[0]
BERNOULLI = False

seed_sim = 42
seed_ecol = 1859
seed_spawn = 376

params = {"n_run": n_run, "length":LENGTH, "dispersal_decay":DISPERSAL_DECAY, "n_spawn":N_SPAWN,
          "ecol_distr":ECOL_DISTR, "seed_sim":seed_sim, "seed_ecol":seed_ecol, "seed_spawn":seed_spawn,
          "bernoulli":BERNOULLI}

#####################################

grid = Grid(length=LENGTH, disp_decay=DISPERSAL_DECAY, ecol_distr=ECOL_DISTR, n_spawn=N_SPAWN, seed_ecol=seed_ecol,
            seed_spawn=seed_spawn)

matplotlib.rcParams['figure.figsize'] = [14.0, 6.0]

plt.imshow(grid.ecol, cmap=cm.get_cmap("Blues"), vmin=0, vmax=1,)
plt.title(f"resource distribution. total resources: {np.rint(np.sum(np.sum(grid.ecol)))}")
plt.show()

log = []
### START SIMULATION
t0 = time.time()
np.random.seed(seed_sim)
for t in range(n_run):
    print(f"iteration {t}")

    grid.step(bernoulli=BERNOULLI, n_jobs=3)
    log.append(np.sum(np.sum(grid.reproduction)))

    # PLOT REPRODUCTIVE POTENTIAL
    if t%plot_freq == 0:
        plot_grid_pop(grid, t, log, n_run, block_img=False)

delta_t = time.time() - t0
print(f"duration of loop: {np.rint(delta_t)} s\naverage iteration duration: {np.round(delta_t/n_run, 2)} s")

# save log, parameters, and population dynamics plot into folder
if save:
    path = "experiments/"
    path += dtt.now().strftime("%d%m%Y_%H%M")
    if description != "":
        path += "_" + description
    path += "/"
    os.mkdir(path)

    param_file = open(path+"params_dict.pck", 'wb')
    pickle.dump(params, param_file)
    param_file.close()

    log_file = open(path+"log.pck", 'wb')
    pickle.dump(log, log_file)
    log_file.close()

    plt.plot(np.array(log), color="black")
    plt.scatter(range(len(log)), np.array(log), color="black")
    plt.title("population dynamics")
    plt.xlim([0, n_run])
    # TODO: ylim based on expected maximum
    plt.savefig(path+"pop_dyn")



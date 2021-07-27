import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from datetime import datetime as dtt
import os
import pickle
import time

from classes import Grid

"""
ecological simulation

2D grid

seasonal organism
"""
save = False
description = "BINARY"  # optional descriptor of current experiment for logging purposes

n_run = 100
plot_freq = 100

LENGTH = 20  # square grid length
DISPERSAL_DECAY = 5  # exponent for decay. higher exponent -> faster decay.
N_SPAWN = 100  # how many cells on the grid are initialised with an organism
ecol_distr_types = ["random_uniform", "random_binary"]
ECOL_DISTR = ecol_distr_types[1]

seed_sim = 42
seed_ecol = 1859
seed_spawn = 378

params = {"n_run": n_run, "length":LENGTH, "dispersal_decay":DISPERSAL_DECAY, "n_spawn":N_SPAWN,
          "ecol_distr":ECOL_DISTR, "seed_sim":seed_sim, "seed_ecol":seed_ecol, "seed_spawn":seed_spawn}

#####################################

grid = Grid(length=LENGTH, disp_decay=DISPERSAL_DECAY, ecol_distr=ECOL_DISTR, n_spawn=N_SPAWN, seed_ecol=seed_ecol,
            seed_spawn=seed_spawn)

matplotlib.rcParams['figure.figsize'] = [14.0, 6.0]

plt.imshow(grid.ecol, cmap=cm.get_cmap("Blues"), vmin=0, vmax=1,)
plt.title(f"resource distribution. total resources: {np.sum(np.sum(grid.ecol))}")
plt.show()

log = []
### START SIMULATION
t0 = time.time()
np.random.seed(seed_sim)
for t in range(n_run):
    print(t)

    grid.step(bernoulli=True, n_jobs=3)
    log.append(np.sum(np.sum(grid.reproduction)))

    # PLOT REPRODUCTIVE POTENTIAL
    if t%plot_freq == 0:
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.suptitle(f"time = {t}")
        ax1.imshow(grid.reproduction, cmap=cm.get_cmap("Greens"), vmin=0,)
        ax1.set_title(f"spatial distribution of reproductive potential")
        ax2.plot(np.array(log))
        ax2.scatter(range(len(log)), np.array(log))
        ax2.set_title("population dynamics")
        ax2.set_xlim([0, n_run])
        plt.show()

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

    plt.plot(np.array(log))
    plt.scatter(range(len(log)), np.array(log))
    plt.title("population dynamics")
    plt.xlim([0, n_run])
    plt.savefig(path+"pop_dyn")


print(f"elapsed time: {time.time()-t0} s")
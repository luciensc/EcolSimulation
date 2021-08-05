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

n_run = 40
plot_freq = 1

LENGTH = 50  # square grid length
DISPERSAL_DECAY = 4  # exponent for decay. higher exponent -> faster decay.
N_SPAWN = 10  # how many cells on the grid are initialised with an organism
ecol_distr_types = ["random_uniform", "random_binary"]
ECOL_DISTR = ecol_distr_types[0]
BERNOULLI = False

seed_ecol = 1859  # initialisation of fitness distribution (grid.ecol)
seed_spawn = 378  # selection of intially populated cells in the grid
seed_sim = 42  # stochastic effects during simulation

save = True
gif = False  # may only be True if 'save' is True
# optional descriptor of current experiment for logging purposes
description = "VARIANCE__decay" + str(DISPERSAL_DECAY) + "_ecol" + str(seed_ecol) + "_spawn" + str(seed_spawn)

#####################################

# TODO: check convention for conditionally required/defined variables
path = None
gif_path = None
if save:
    path = "experiments/"
    path += dtt.now().strftime("%d%m%Y_%H%M")
    if description != "":
        path += "_" + description
    path += "/"
    os.mkdir(path)

    # save each iteration's plot
    if gif:
        gif_path = path + "gif/"
        os.mkdir(gif_path)


grid = Grid(length=LENGTH, disp_decay=DISPERSAL_DECAY, ecol_distr=ECOL_DISTR, n_spawn=N_SPAWN, seed_ecol=seed_ecol,
            seed_spawn=seed_spawn)

matplotlib.rcParams['figure.figsize'] = [14.0, 6.0]

# plot initial resource distribution
# plt.imshow(grid.ecol, cmap=cm.get_cmap("Blues"), vmin=0, vmax=1,)
max_resources = np.sum(np.sum(grid.ecol))
# plt.title(f"resource distribution. total resources: {int(np.rint(max_resources))}")
# plt.show()

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
        plot_grid_pop(grid, t, log, n_run, save_path=gif_path, ylim=max_resources, block_img=False)

delta_t = time.time() - t0
print(f"duration of loop: {np.rint(delta_t)} s\naverage time per iteration: {np.round(delta_t/n_run, 2)} s")

# save log, parameters, and population dynamics plot into folder
if save:
    params = {"n_run": n_run, "length": LENGTH, "dispersal_decay": DISPERSAL_DECAY, "n_spawn": N_SPAWN,
              "ecol_distr": ECOL_DISTR, "seed_sim": seed_sim, "seed_ecol": seed_ecol, "seed_spawn": seed_spawn,
              "bernoulli": BERNOULLI}
    param_file = open(path + "params_dict.pck", 'wb')
    pickle.dump(params, param_file)
    param_file.close()

    log_file = open(path + "log.pck", 'wb')
    pickle.dump(log, log_file)
    log_file.close()

    plt.close()
    plt.plot(np.array(log), color="black")
    plt.scatter(range(len(log)), np.array(log), color="black")
    plt.title("population dynamics")
    plt.xlim([0, n_run])
    plt.ylim([0, max_resources])
    plt.savefig(path + "pop_dyn")



"""
investigate population dynamics - compare with theoretical, non-spatial models
"""


import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm
import numpy as np

from aux_grid import Grid
from aux_plotting_functions import plot_grid_pop

LENGTH = 50  # square grid length
DISPERSAL_DECAY = 4  # exponent for decay. higher exponent -> faster decay.
N_SPAWN = 1  # how many cells on the grid are initialised with an organism
ecol_distr_types = ["random_uniform", "random_binary"]
ECOL_DISTR = ecol_distr_types[0]
seed_ecol = 1859  # initialisation of fitness distribution (grid.ecol)
seed_spawn = 380  # selection of initially populated cells in the grid.

grid = Grid(length=LENGTH, disp_decay=DISPERSAL_DECAY, ecol_distr=ECOL_DISTR, n_spawn=N_SPAWN, seed_ecol=seed_ecol,
            seed_spawn=seed_spawn)

# grid_log = []
# log = []
# n_run = 50
# matplotlib.rcParams['figure.figsize'] = [14.0, 6.0]
#
# for t in range(n_run):
#     print(f"iteration {t}")
#
#     grid.step(bernoulli=False, n_jobs=1)
#     log.append(np.sum(np.sum(grid.reproduction)))
#     grid_log.append(grid.reproduction)
#     # PLOT REPRODUCTIVE POTENTIAL
#     # plot_grid_pop(grid, t, log, n_run, save_path=None, ylim=1500, block_img=False)
#     distr = grid.reproduction.flatten()
#     distr = distr[distr>0]
#     if t%10 == 0:
#         plt.hist(distr, range=[0,1], bins=20)
#         plt.show()


# ### PLOT GRID: EXPLAIN CONCEPT BEHIND ECOL. POTENTIAL. DIFFERENT COLOR.
# matplotlib.rcParams['figure.figsize'] = [14.0, 6.0]
#
# plt.imshow(grid.ecol, cmap=cm.get_cmap("Blues"), vmin=0, )
# plt.savefig("media/ecol_distribution.png", dpi=300)


### ANALYSE POPULATION DYNAMICS CURVE
# evaluate reproduction coefficient

# neighbour_coeff = (1 + 1*(1+d_1,1)^-4 + ...)
# reproductive potential = ecol_0,0 * neighbour_coeff
neighbour_coeff = 1
# disperse potential -> sum up
for p, q in grid.neighbours(0, 0):  # considering only moore k-neighbours
    # => considerable speed up for larger grids
    neighbour_coeff += 1 * np.power((1 + grid.distance(0, 0, p, q)), -1 * DISPERSAL_DECAY)


# simulate exponential growth based on mean:
deterministic_pop_sim = [1]
for i in range(50):
    temp = deterministic_pop_sim[-1] + deterministic_pop_sim[-1] * 0.5 * neighbour_coeff
    deterministic_pop_sim.append(temp)

#
# # TODO:
# #  REPRODUCTION COEFFICIENT DOES NOT STAY CONSTANT AT ALL: NEXT SPAWNED INDIVIDUALS ARE LESS LIKELY TO PROCREATE BC LESS INIT => COLLAPSE OF REPRODUCTIVE VALUE
#
# # simulate logistic growth based on mean:
# logistic_pop_sim = [1]
# K=1200
# for i in range(50):
#     temp = logistic_pop_sim[-1] + logistic_pop_sim[-1] * 0.5 * neighbour_coeff*(K-logistic_pop_sim[-1])/K
#     logistic_pop_sim.append(temp)
#
#
# # simulate growth with variation:
# stochastic_pop_sim = [1]
# for i in range(50):
#     temp = stochastic_pop_sim[-1] + stochastic_pop_sim[-1] * np.random.random(1)[0] * neighbour_coeff
#     stochastic_pop_sim.append(temp)
#
# plt.plot(deterministic_pop_sim)
# plt.plot(stochastic_pop_sim)
# plt.plot(logistic_pop_sim)
# plt.ylim([0, 1400])
# plt.show()




# evaluate empirirical r based on slope

# exponential

# logistic

# logistic with variation
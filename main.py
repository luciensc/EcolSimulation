import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm

from classes import Grid

"""
ecological simulation

2D grid

seasonal organism
"""
N_RUN = 30
PLOT_FREQ = 5

LENGTH = 50  # square grid length
DISPERSAL_DECAY = 3  # exponent for decay. higher exponent -> faster decay.
N_SPAWN = 10  # how many cells on the grid are initialised with an organism
ecol_distr_types = ["random_uniform", "random_binary"]
ECOL_DISTR = ecol_distr_types[0]

#####################################
# *currently* obsolete: fitness function not specified
# as fitness currently solely depends on resource: fitness modeled directly
# in future: introduce same/different species interaction for fitness effect -> re-use the function
# def fitness(ecol_ij, fit="binary", threshold=0.7):
#     # different concepts of fitness possible
#     # ought add stochasticity to fitness component??
#     if fit=="binary":
#         # assume binary fertile / infertile if above/below threshold
#         out = int(ecol_ij>threshold)
#     elif fit=="linear":
#         out = ecol_ij
#     else:
#         return Exception(f"no valid fitness type specified: {FITNESS_TYPE}")
#     return out

# vfit = np.vectorize(fitness)
# grid_fit = vfit(grid.ecol, fit=FITNESS_TYPE)
# plt.imshow(grid_fit, cmap=cm.get_cmap("Blues"), vmin=0, vmax=1,)
# plt.title("fitness distribution")
# plt.show()
#####################################

grid = Grid(length=LENGTH, disp_decay=DISPERSAL_DECAY, ecol_distr=ECOL_DISTR, n_spawn=N_SPAWN)

matplotlib.rcParams['figure.figsize'] = [8.0, 6.0]

plt.imshow(grid.ecol, cmap=cm.get_cmap("Blues"), vmin=0, vmax=1,)
plt.title("resource distribution")
plt.show()

log = []
### START SIMULATION
for t in range(N_RUN):
    print(t)
    grid.step(bernoulli=True)

    # PLOT REPRODUCTIVE POTENTIAL
    if t%PLOT_FREQ == 0:
        plt.imshow(grid.reproduction, cmap=cm.get_cmap("Greens"), vmin=0,)
        plt.title(f"population distribution at time {t}")
        plt.show()
        # TODO: plot pop. dynamics over time next to it

    log.append(np.sum(np.sum(grid.biol)))


plt.plot(np.array(log))
plt.scatter(range(len(log)), np.array(log))
plt.title("population dynamics over time")
plt.show()
print("")
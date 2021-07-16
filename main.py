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

LENGTH = 20
DISPERSAL_DECAY = 3  # exponent for decay. higher exponent -> faster decay.
ECOL_THRESHOLD = 0.7
N_RUN = 50
PLOT_FREQ = 10
#N_SPAWN = 5

#####################################
def fitness(ecol_ij):
    # different concepts of fitness possible
    # in this case: assume binary fertile / infertile if within .2 of ECOL_PREF
    # ought add stochasticity to fitness component??
    return int(ecol_ij>ECOL_THRESHOLD)
#####################################

grid = Grid(length=LENGTH, disp_decay=DISPERSAL_DECAY)

plt.imshow(grid.ecol, cmap=cm.get_cmap("Blues"), vmin=0, vmax=1,)
plt.title("resource distribution")
plt.show()

log = []
### START SIMULATION
for t in range(N_RUN):
    print(t)
    grid.step(fitness_fxn=fitness, bernoulli=True)

    # PLOT REPRODUCTIVE POTENTIAL
    if t%PLOT_FREQ == 0:
        plt.imshow(grid.reproduction, cmap=cm.get_cmap("Greens"), vmin=0,)
        plt.title(f"population distribution at time {t}")
        plt.show()

    log.append(np.sum(np.sum(grid.biol)))


plt.plot(np.array(log))
plt.scatter(range(len(log)), np.array(log))
plt.title("population dynamics over time")
plt.show()
print("")
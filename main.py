import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm

"""
ecological simulation

2D grid

seasonal plant
"""

LENGTH = 20
N_SPAWN = 5
DISPERSAL_DECAY = 3  # exponent for decay. higher exponent -> faster decay.
ECOL_THRESHOLD = 0.7
N_RUN = 50
PLOT_FREQ = 50

########################################
def random_pos():
    return np.random.randint(LENGTH, size=2)

def fitness(ecol_ij):
    # different concepts of fitness possible
    # in this case: assume binary fertile / infertile if within .2 of ECOL_PREF
    return int(ecol_ij>ECOL_THRESHOLD)

def distance(i,j,p,q):
    return np.linalg.norm(np.array([i,j])-np.array([p,q]))

all_cells = []
for i in range(LENGTH):
    for j in range(LENGTH):
        all_cells.append((i,j))

def neighbours(i,j):
    neigh = 5  # moore neighbourhood
    i_low = np.clip(i-neigh, 0, LENGTH)
    i_high = np.clip(i+neigh+1, 0, LENGTH)  # +1 bc range(a, b+1) -> a, .., b
    j_low = np.clip(j-neigh+1, 0, LENGTH)
    j_high = np.clip(j+neigh+1, 0, LENGTH)
    neighbours = []
    for i_new in range(i_low, i_high):
        for j_new in range(j_low, j_high):
            neighbours.append((i_new, j_new))
    return neighbours


########################################


# init
np.random.seed(1859)
grid_ecol = np.random.random((LENGTH, LENGTH))

grid_biol = np.zeros(grid_ecol.shape)
# spawn initial occurring plant spots
for i in range(N_SPAWN):
    R = random_pos()
    grid_biol[R[0], R[1]] = 1

plt.imshow(grid_ecol, cmap=cm.get_cmap("Blues"), vmin=0, vmax=1,)
plt.show()

plt.imshow(grid_biol, cmap=cm.get_cmap("Greens"), vmin=0, vmax=1,)
plt.show()

log = []

### START SIMULATION
for t in range(N_RUN):
    print(t)
    # grow -> reproduce
    grid_reproduction = np.full(grid_ecol.shape, np.nan)  # reproduction_ij = biol_ij*fitness(ecol_ij)
    for i, j in all_cells:
            grid_reproduction[i,j] = grid_biol[i,j]*fitness(grid_ecol[i,j])
            # add general stochasticity to fitness component???

    # PLOT REPRODUCTIVE POTENTIAL
    if t%PLOT_FREQ == 0:
        plt.imshow(grid_reproduction, cmap=cm.get_cmap("Greens"), vmin=0,)
        plt.title(t)
        plt.show()


    # disperse
    grid_biol_NEW = np.zeros(shape=grid_biol.shape)
    # for each cell: add decayed fitness to all cells (incl. self)
    # TODO: in parallel?
    for i, j in all_cells:
            for p, q in neighbours(i,j): # considering only local neighbours => considerable speed up for larger grids
                    grid_biol_NEW[p,q] \
                        += grid_reproduction[i,j]*1/np.power((1+distance(i,j,p,q)), DISPERSAL_DECAY)

    grid_biol = np.clip(grid_biol_NEW, a_min=0, a_max=1)
    grid_biol = np.random.binomial(1, grid_biol)  # bernoulli sampling for stochastic component
    # TODO: ADD COMPETITION btw at least two species. impose some restrictions on fitness distribution
    # TODO: TRY RESILIENCE UNDER DIFFERENT MODES OF REPRODUCTION / LANDSCAPE DISTRIBUTIONS
        # E.G. ORCHIDS: LOW DISPERSAL COEFFICIENT, SPARSE LANDSCAPES => EFFECT OF PERTURBATION TO POPULATION / INFRASTRUCTURE
        # demonstrate that strategy can evolve: e.g. trade-off of growth speed & dispersal-decay

    log.append(np.sum(np.sum(grid_biol)))


plt.plot(np.array(log))
plt.scatter(range(len(log)), np.array(log))
plt.show()
print("")
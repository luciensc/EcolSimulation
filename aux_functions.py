import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
# save function

# plot functions
def plot_grid_pop(grid, iter, log, n_run, block_img=False, save=False):
    """
    plot the spatial representation (left subplot) and population over time (right subplot)
    """
    plt.close()
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(f"iteration = {iter}")
    ax1.imshow(grid.reproduction, cmap=cm.get_cmap("Greens"), vmin=0, )
    ax1.set_title(f"spatial distribution of reproductive potential")
    ax2.plot(np.array(log))
    ax2.scatter(range(len(log)), np.array(log))
    ax2.set_title("population dynamics")
    ax2.set_xlim([0, n_run])
    plt.show(block=block_img)
    plt.pause(0.00001)
    # TODO: implement saving function. requires path.
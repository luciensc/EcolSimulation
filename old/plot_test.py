import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10*np.pi, 100)
plt.show(block=False)
for phase in np.linspace(0, 10*np.pi, 100):
    plt.plot(x, np.sin(0.5 * x + phase))
    plt.pause(0.1)  # plt.pause(): temporarily suspends all threads, not just plotting (tested in main file)
    plt.close()


# plt.ion(): only for console?
# plt.show():
#   default: plt.show(block=True) => waits until window is closed

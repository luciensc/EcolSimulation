# plot sigmoid curves comparing binary fitness with continuous fitness under otw identical parametrisation

import matplotlib.pyplot as plt
import pickle as p
root = "experiments/"

# folders_binary = ["22072021_1731_binaryfitness", "22072021_1733_binaryfitness_2", "22072021_1733_binaryfitness_3"]
# folders_continuous = ["22072021_1736_continuousfitness_3", "22072021_1737_continuousfitness_2",
#                       "22072021_1738_continuousfitness_1"]


# binary folders
for nm in folders_binary:
    log_file = open(root+nm+"/log.pck", 'rb')
    log = p.load(log_file)
    #binary_logs.append(log)
    log_file.close()
    plt.plot(log, color="black")

# continuous folders
for nm in folders_continuous:
    log_file = open(root+nm+"/log.pck", 'rb')
    log = p.load(log_file)
    #binary_logs.append(log)
    log_file.close()
    plt.plot(log, color="blue")

plt.title("dynamics. black: binary, blue: continuous.")
plt.show()
print("")

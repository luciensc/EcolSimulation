import imageio
import os

folder_path = "experiments/05082021_1101_VARIANCE__decay4_ecol1859_spawn376/"
filenames = os.listdir(folder_path+"gif/")
filenames.sort()
with imageio.get_writer(folder_path+"dyn.gif", mode='I', duration="0.3") as writer:
    for filename in filenames:
        assert filename[-4:] == ".png"
        print(filename)
        image = imageio.imread(folder_path + "gif/" + filename)
        writer.append_data(image)
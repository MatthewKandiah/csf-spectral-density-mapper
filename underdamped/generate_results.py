import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys

### pull number of plot points from command line variables

if __name__ == "__main__":
	NUMBER_OF_PLOT_POINTS = int(sys.argv[1])

plot_points = np.zeros((NUMBER_OF_PLOT_POINTS, 2))

for i in range(0,NUMBER_OF_PLOT_POINTS):
	in_file = open(f"./picklejar/plot_point_{i}.pickle", rb)
	plot_point = pickle.load(in_file)
	plot_points[i][0] = plot_point[0]
	plot_points[i][1] = plot_point[1]
	in_file.close()

plot_points.sort(key = lambda x: x[0])

plot_points.tofile('./results/mapped_underdamped_spectral_density.csv', sep = ',')

plt.savefig('./results/mapped_underdamped_spectral_density.png')

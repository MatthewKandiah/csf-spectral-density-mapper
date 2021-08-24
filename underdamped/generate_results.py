import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys

### pull number of plot points from command line variables

if __name__ == "__main__":
	NUMBER_OF_PLOT_POINTS = int(sys.argv[1])

plot_points = np.zeros((2, NUMBER_OF_PLOT_POINTS))

for i in range(0,NUMBER_OF_PLOT_POINTS):
	in_file = open(f"./picklejar/plot_point_{i}.pickle", 'rb')
	plot_point = pickle.load(in_file)
	plot_points[0][i] = plot_point[0]
	plot_points[1][i] = plot_point[1]
	in_file.close()

plot_points = plot_points[::, plot_points[0,].argsort()]

plot_points.tofile('./results/mapped_underdamped_spectral_density.csv', sep = ',')

plt.plot(plot_points)
plt.savefig('./results/mapped_underdamped_spectral_density.png')

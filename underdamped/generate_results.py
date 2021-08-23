import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys

'''
pull number of plot points from command line variables
'''
if __name__ == "__main__":
	NUMBER_OF_PLOT_POINTS = int(sys.argv[1])

plot_points = np.array() 
### np.array can't be called with zero parameters. Maybe better to do a list, convert to np.array, then generate csv

for i in range(0,NUMBER_OF_PLOT_POINTS):
	in_file = open(f"/picklejar/plot_point_{i}.pickle", rb)
	plot_point = pickle.load(in_file)
	np.append(plot_points, plot_point)
	in_file.close()

plot_points.sort(key = lambda x: x[0])

plot_points.tofile('results/mapped_underdamped_spectral_density.csv', sep = ',')

plt.savefig('results/mapped_underdamped_spectral_density.png')

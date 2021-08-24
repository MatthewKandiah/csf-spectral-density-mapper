import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys
import csv

### pull number of plot points from command line variables

if __name__ == "__main__":
	NUMBER_OF_PLOT_POINTS = int(sys.argv[1])

plot_points = []

for i in range(0,NUMBER_OF_PLOT_POINTS):
	in_file = open(f"./picklejar/plot_point_{i}.pickle", 'rb')
	plot_point = pickle.load(in_file)
	plot_points.append(plot_point)
	in_file.close()

### plot results

plt.plot([x[0] for x in plot_points],[y[0] for y in plot_points])
plt.xlabel('Frequency')
plt.ylabel('Mapped spectral density')
plt.savefig('./results/mapped_underdamped_spectral_density.png')

### write results to csv

with open("./results/mapped_underdamped_spectral_density.csv", "w") as out_file:
	writer = csv.writer(out_file)
	writer.writerows()

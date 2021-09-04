import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

### run this in the underdamped directory, in the place where this file is saved
### otherwise the paths won't be defined correctly

plot_points_frame = pd.read_csv('./results/mapped_underdamped_spectral_density.csv')
plot_points_array = plot_points_frame.values
frequencies = plot_points_array[:,0]
rc_frequencies = plot_points_array[:,1]

plt.title('Mapping an Underdamped Spectral Density')
plt.xlabel('Frequency')
plt.ylabel('Mapped Spectral Density')
plt.axis([ 0, 1.1, 0, 0.17 ])
plt.plot(frequencies,rc_frequencies)
plt.savefig('./results/mapped_underdamped_spectral_density.png')

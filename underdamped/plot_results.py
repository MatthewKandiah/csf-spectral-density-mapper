import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

### run this in the same directory as your csv containing your plot points

plot_points_frame = pd.read_csv('./results/mapped_underdamped_spectral_density.csv')
plot_points_array = plot_points_frame.values
frequencies = plot_points_array[:,0]
rc_frequencies = plot_points_array[:,1]

print(frequencies)
print(rc_frequencies)

plt.title('Mappeing an Underdamped Spectral Density')
plt.xlabel('frequency')
plt.ylabel('mapped spectral density')
# plt.xticks(np.arange(0, 1, step=0.2))
# plt.yticks(np.arange(0,0.16, step=0.02))
plt.axis([0,1,0,0.16])
plt.plot(frequencies,rc_frequencies)
plt.savefig('test.png')
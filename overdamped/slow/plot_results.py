import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

### run this in the underdamped directory, in the place where this file is saved
### otherwise the paths won't be defined correctly

plot_points_frame = pd.read_csv('./results/mapped_overdamped_slow_spectral_density.csv')
plot_points_array = plot_points_frame.values
cutoff_frequencies = plot_points_array[:,0]
first_moments = plot_points_array[:,1]
reorganisation_energies = plot_points_array[:,2]
rc_frequencies = plot_points_array[:,3]
rc_system_coupling_strengths = plot_points_array[:,4]

### plot cutoff against first-moment
plt.title('Cutoff vs First Moment')
plt.xlabel('Cutoff Frequency')
plt.ylabel('First Moment of Unmapped Spectral Density')
plt.plot(cutoff_frequencies,first_moments)
plt.savefig('./results/cutoff_vs_first_moment.png')
plt.clf()

### plot cutoff against reorganisation energy
plt.title('Cutoff vs Reorganisation Energy')
plt.xlabel('Cutoff Frequency')
plt.ylabel('Reorganisation Energy')
plt.plot(cutoff_frequencies,reorganisation_energies)
plt.savefig('./results/cutoff_vs_reorganisation_energy.png')
plt.clf()

### plot cutoff against rc frequency
plt.title('Cutoff vs RC Frequency')
plt.xlabel('Cutoff Frequency')
plt.ylabel('RC Frequency')
plt.plot(cutoff_frequencies,rc_frequencies)
plt.savefig('./results/cutoff_vs_rc_frequency.png')
plt.clf()

### plot cutoff against rc-system coupling strength
plt.title('Cutoff vs RC Coupling Strength')
plt.xlabel('Cutoff Frequency')
plt.ylabel('RC Coupling Strength')
plt.plot(cutoff_frequencies,rc_system_coupling_strengths)
plt.savefig('./results/cutoff_vs_rc_coupling_strength.png')
plt.clf()

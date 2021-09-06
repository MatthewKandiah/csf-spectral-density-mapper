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
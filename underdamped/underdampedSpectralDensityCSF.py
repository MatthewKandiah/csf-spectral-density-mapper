import rcmapping
import sys
import numpy as np
import pickle

PLOT_FREQUENCIES = np.arange(0.1, 1.1, 0.1)

'''
pull frequency from command line variables
'''
if __name__ == "__main__":
	index = int(sys.argv[1])
	omega = PLOT_FREQUENCIES[index]

'''
define constants for this calculation
'''
ALPHA = 0.01
GAMMA = 5
OMEGA0 = 5

underdamped_spectral_density = rcmapping.SpectralDensity(
	lambda omega, alpha, gamma, omega0: 
		alpha * gamma * omega0**2 * omega / ((omega0**2 - omega**2)**2 + (gamma*omega)**2),
	ALPHA, GAMMA, OMEGA0
	)

mapped_spectral_density = rcmapping.Mapping(underdamped_spectral_density)
mapped_spectral_density_point = mapped_spectral_density.calculate_mapped_spectral_density(omega)

print(omega, mapped_spectral_density_point)

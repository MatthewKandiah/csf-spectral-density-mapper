import rcmapping
import sys
import numpy as np
import pickle

PLOT_CUTOFF_FREQUENCIES = np.arange(0.1, 100.1, 1)

'''
pull index from command line variables
'''
if __name__ == "__main__":
	index = int(sys.argv[1])
	CUTOFF_FREQUENCY = PLOT_CUTOFF_FREQUENCIES[index]
	PICKLE_NAME = f"./picklejar/result_{index}.pickle"
'''
define constants for this calculation
'''
ALPHA = 0.01
OMEGAC = 2

slow_cutoff = lambda omega, cutoff: np.exp(-omega/cutoff)

overdamped_slow_spectral_density = rcmapping.SpectralDensity(
	lambda omega, alpha, omegac, cutoff:
		slow_cutoff(omega,cutoff) * alpha * omegac * omega / (omega**2 + omegac**2),
	ALPHA, OMEGAC, CUTOFF_FREQUENCY
	)

mapped_spectral_density = rcmapping.Mapping(overdamped_slow_spectral_density)

result_row = [
				CUTOFF_FREQUENCY, 
				mapped_spectral_density.first_moment,
				mapped_spectral_density.reorganisation_energy,
				mapped_spectral_density.rc_frequency,
				mapped_spectral_density.rc_system_coupling_strength
			]

output_file = open(PICKLE_NAME, 'wb')
pickle.dump(result_row, output_file)
output_file.close()

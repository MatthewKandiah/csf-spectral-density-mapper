import numpy as np
import scipy.integrate as integrate

class SpectralDensity:
	def __init__(self, function, *args):
		self.function = function
		self.parameters = args

	def calculate_value(self, omega):
		return self.function(omega, *self.parameters)

	def calculate_first_moment(self):
		return integrate.quad(lambda omega: self.calculate_value(omega)*omega, 0, np.inf )[0]

	def calculate_reorganisation_energy(self):
		return integrate.quad(lambda omega: self.calculate_value(omega)/omega, 0, np.inf )[0]


class Mapping:
	def __init__(self, spectral_density):
		self.spectral_density = spectral_density
		self.first_moment = self.spectral_density.calculate_first_moment()
		self.reorganisation_energy = self.spectral_density.calculate_reorganisation_energy()
		self.rc_frequency = self.calculate_rc_frequency()
		self.rc_system_coupling_strength = self.calculate_rc_system_coupling_strength()

	def calculate_rc_frequency(self):
		return np.sqrt(self.first_moment / self.reorganisation_energy)

	def calculate_rc_system_coupling_strength(self):
		return np.sqrt(self.first_moment / self.rc_frequency)

	def calculate_mapped_spectral_density(self, omega):
		principal_value_integral = integrate.quad(lambda x: self.spectral_density.calculate_value(x), -1000, 1000, weight = 'cauchy', wvar = omega)[0]
		denominator = (np.pi * self.spectral_density.calculate_value(omega))**2 + principal_value_integral**2
		return (self.rc_system_coupling_strength**2 * self.spectral_density.calculate_value(omega)/denominator)

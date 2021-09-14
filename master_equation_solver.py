import numpy as np
import qutip as qt

class Bath:
	def __init__(self, spectral_density, temperature):
		self.spectral_density = spectral_density
		self.temperature = temperature

class State(qt.Qobj):
	def check_valid(self):
		if self.shape[0] != self.shape[1]:
			raise ValueError(f"State expects square matrix. Received {self.data}")
		if self.isherm == False:
			raise ValueError(f"State expects Hermitian matrix. Received {self.data}")

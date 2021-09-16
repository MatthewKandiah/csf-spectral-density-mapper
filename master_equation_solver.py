import numpy as np
import qutip as qt

class Bath:
	def __init__(self, spectral_density, temperature):
		self.spectral_density = spectral_density
		self.temperature = temperature


class State(qt.Qobj):
	def check_valid(self, tolerance=0):
		if self.shape[0] != self.shape[1]:
			raise ValueError(f"State expects square matrix. Received {self.data}")
		if self.isherm == False:
			raise ValueError(f"State expects Hermitian matrix. Received {self.data}")
		if abs(self.tr() - 1) > tolerance:
			raise ValueError(f"State expected to be normalised up to errors of the order {tolerance}. Received matrix with trace = {self.tr()}")


def steady_state_solver(Liouvillian, solver_method, absolute_tolerance):
	rhoSS_steady = qt.steadystate(
		liouvillian, 
		method=solver_method, 
		sparse=True, 
		tol = absolute_tolerance,
		maxiter = 100000,
		use_precond = True)
    return rhoSS_steady

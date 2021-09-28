import numpy as np
import qutip as qt

class Bath:
	def __init__(self, spectral_density, temperature):
		self.spectral_density = spectral_density
		self.temperature = temperature


def steady_state_solver(Liouvillian, solver_method, absolute_tolerance):
	rhoSS_steady = qt.steadystate(
		liouvillian, 
		method=solver_method, 
		sparse=True, 
		tol = absolute_tolerance,
		maxiter = 100000,
		use_precond = True
		)
	return rhoSS_steady

sigx = qt.sigmax()
sigy = qt.sigmay()
sigz = qt.sigmaz()
id2  = qt.qeye(2)

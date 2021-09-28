import numpy as np
import qutip as qt
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from master_equation_solver import *
from rcmapping import *

'''
define parameters 
'''
f1 = 0.6
f2 = 0.4
omega0 = 1

# system Hamiltonian
HamS = omega0 / (2 * np.sqrt(f1**2 + f2**2)) * (f1 * sigz - f2 * sigx)

# augmented system Hamiltonian

# numerically calculate eigensystem of augmented Hamiltonian

# construct bath operators (truncated)

# calculate master equation rate operators

# construct Liouvillian from master equation

# solve master equation

# rotate steady state basis to compare to Guarnieri's weak coupling results
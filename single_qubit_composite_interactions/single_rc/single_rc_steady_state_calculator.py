import numpy as np
import qutip as qt
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import master_equation_solver as mes
import rcmapping as rcm

def calculate_steady_state_single_rc(HamS, HamIS, bath, truncation_level):
	# RC operators
	destroy = qt.destroy(truncation_level)
	create = qt.create(truncation_level)
	number = create * destroy
	id_rc = qt.qeye(truncation_level)

	BETA = 1/bath.temperature

	# RC mapping
	mapping = rcm.Mapping(bath.spectral_density)

	# augmented system Hamiltonian
	HamSS = (
            qt.tensor(HamS, id_rc) 
            +mapping.rc_frequency * qt.tensor(mes.id2, number)
            +mapping.rc_system_coupling_strength * qt.tensor(HamIS, create + destroy)
        )

	# numerically calculate eigensystem of augmented Hamiltonian
	eigenvalues, eigenstates = HamSS.eigenstates(sparse = True, tol = 1e-20, maxiter = 100000)

	# construct bath operators (truncated)
	operator_A = qt.tensor(mes.id2, create + destroy)

	# calculate master equation rate operators
	operator_chi = 0
	operator_xi = 0

	for j in range(0, len(eigenstates)):
	    for k in range (0, len(eigenstates)):
	        bra_j = eigenstates[j].dag()
	        ket_k = eigenstates[k]
	        Ajk = bra_j * operator_A * ket_k

	        # consider cases where eigenvalues are equal or different separately for calculating contributions to chi operators 
	        if eigenvalues[j] != eigenvalues[k]:
	            operator_chi += ((np.pi/2) 
	                            * (mapping.rc_system_coupling_strength * Ajk * (eigenvalues[j] - eigenvalues[k]) 
	                            / np.tanh(BETA * (eigenvalues[j] - eigenvalues[k]) / 2)) 
	                            * (eigenstates[j] * eigenstates[k].dag()))

	        # if the two eigenvalues are the same, then tanh(0) = 0 so we will get a value error because you aren't allowed to divide by zero. Need to manually account for the fact that x*coth(x) is equal to 1 at x=0.
	        # this case is guaranteed to arise when j == k. If HamSS is degenerate, there may other cases too.
	        else:
	            operator_chi += ((np.pi/2) 
	                            * (mapping.rc_system_coupling_strength * Ajk) * (2/BETA) 
	                            *(eigenstates[j] * eigenstates[k].dag()))

	            # all eigenvalue pairs can be treated the same way when calulating Xi operators
	            operator_xi += ((np.pi/2) 
	                            * (mapping.rc_system_coupling_strength * Ajk 
	                            * (eigenvalues[j] - eigenvalues[k])) 
	                            * (eigenstates[j] * eigenstates[k].dag()))

	# construct Liouvillian from master equation
	unitary_liouvillian = -1j * qt.spre(HamSS) + 1j * qt.spost(HamSS)
	interaction_liouvillian = ( - qt.spre(operator_A * operator_chi) 
	                            + qt.spre(operator_A)*qt.spost(operator_chi) 
	                            + qt.spre(operator_chi)*qt.spost(operator_A) 
	                            - qt.spost(operator_chi * operator_A) 
	                            - qt.spre(operator_A * operator_xi) 
	                            - qt.spre(operator_A)*qt.spost(operator_xi) 
	                            + qt.spre(operator_xi)*qt.spost(operator_A) 
	                            + qt.spost(operator_xi * operator_A))

	liouvillian = unitary_liouvillian + interaction_liouvillian

	# solve master equation
	steady_state = (mes.steady_state_solver(liouvillian, "iterative-gmres", 1e-20)).ptrace(0)
	return steady_state

if __name__ == "__main__":
	# system Hamiltonian
	f1 = 6.
	f2 = 4.
	ALPHA = 0.01
	GAMMA = 0.5
	OMEGA0 = 1.
	HamS = OMEGA0 / (2 * np.sqrt(f1**2 + f2**2)) * (f1 * mes.sigz - f2 * mes.sigx)

	# system part of interaction Hamiltonian
	HamIS = np.sqrt(f1**2 + f2**2) * mes.sigz

	# specify bath parameters
	underdamped_spectral_density = rcm.SpectralDensity(
	    lambda omega, alpha, gamma, omega0: 
	        alpha * gamma * omega0**2 * omega / ((omega0**2 - omega**2)**2 + (gamma*omega)**2),
	    ALPHA, GAMMA, OMEGA0
	    )
	TEMPERATURE = 0.001

	bath = mes.Bath(underdamped_spectral_density, TEMPERATURE)
	print (calculate_steady_state_single_rc(HamS, HamIS, bath, 20))
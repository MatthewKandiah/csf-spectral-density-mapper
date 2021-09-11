import unittest
import numpy as np
import master_equation_solver as mes

class DensityOperator(unittest.TestCase):

	def test_density_operator(self):
		array = np.array([[0.7,0.2+0.1j],[0.2-0.1j, 0.3]])
		rho = mes.density_operator(array)
		self.assertEqual(rho.trace, 1)
		self.assertEqual(rho.dimension, 2)
		self.assertTrue(rho.isHermitian)

	def test_bad_density_operator(self):
		array =np.array([[0.2, 8j],[4, 1.3]])
		rho = mes.density_operator(array)
		self.assertEqual(rho.trace, 1.5)
		self.assertEqual(rho.dimension, 2)
		self.assertFalse(rho.isHermitian)


if __name__ == '__main__':
	unittest.main()

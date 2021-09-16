import unittest
import numpy as np
import qutip as qt
import master_equation_solver as mes

class TestState(unittest.TestCase):
	def test_shape_throws_error(self):
		state = mes.State(np.zeros((2,3)))
		self.assertEqual(state.shape, (2,3))
		self.assertRaises(ValueError, state.check_valid)

	def test_shape_valid(self):
		state = mes.State(np.zeros((2,2)))
		self.assertEqual(state.shape, (2,2))
		# next line should not raise an error
		state.check_valid

	def test_isherm_throws_error(self):
		state = mes.State(np.array([[1+2j, 0],[0, 1]]))
		self.assertRaises(ValueError, state.check_valid)

	def test_isherm_valid(self):
		state = mes.State(np.array([[1, 0+1j],[0-1j, 2]]))
		# next line should not raise an error
		state.check_valid

	def test_trace_throws_error(self):
		state = mes.State(np.array([[1,2],[3,4]]))
		self.assertRaises(ValueError, state.check_valid)

	def test_trace_valid(self):
		state = mes.State(np.array([[0.5, 1],[1, 0.5]]))
		# next line should not raise an error
		state.check_valid

	def test_trace_with_tolerance_throws_error(self):
		state = mes.State(np.array([[0.5, 1],[1, 0.6]]))
		with self.assertRaises(ValueError):
			state.check_valid(0.01)

	def test_trace_with_tolerance_valid(self):
		state = mes.State(np.array([[0.5, 1],[1, 0.6]]))
		# next line should not raise an error
		state.check_valid(0.2)


if __name__ == '__main__':
	unittest.main()

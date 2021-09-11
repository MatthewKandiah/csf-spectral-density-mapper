import numpy as np

class density_operator:

	def __init__(self, array):
		self.array = array
		self.dimension = self.array.ndim
		self.trace = np.trace(self.array)
		self.isHermitian = (self.array.conjugate().transpose() == self.array).all()


class vectorised_density_operator:

	def __init__(self, array):
		self.array = array

	def _vectorise_matrix(self):
		pass



class Board():
	"""
	Board class with board state and helper functions
	"""

	def __init__(self):
		"""
		Sets up an empty board.
		"""

		self.board = []

		# Filling the board

		for i in range(3):
			self.board.append([0,0,0])

	def get_board(self):
		"""
		Returns the board 3x3 array.
		"""
		return self.board


	def output(self):
		"""
		Prints the board onto the Terminal.
		"""

		for i in self.board:
			for j in i:
				p = "-"
				if (j == 1): p = "x"
				elif (j == 2): p = "o"
				print(p, end="")
			print()


	def input(self, p, x, y):
		"""
		Processes new input.
		"""

		self.board[y][x] = p
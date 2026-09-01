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

		for i in range(3): # Fills up a 3x3 matrix with 0s
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
			for j in i: # Loops through the matrix
				p = "-" # Empty slots displayed as -
				if (j == 1): p = "x" # Player is x
				elif (j == 2): p = "o" # Algorithm is o
				print(p, end="")
			print() # switch to next line


	def input(self, p, x, y):
		"""
		Processes new input.
		"""

		self.board[y][x] = p # Changes board state at given coordinates
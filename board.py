

class Board():

	def __init__(self):
		self.board = []

		# Filling the board

		for i in range(3):
			self.board.append([0,0,0])

	def get_board(self):
		return self.board


	def output(self):

		# Outputting the current board State

		for i in self.board:
			for j in i:
				p = "-"
				if (j == 1): p = "x"
				elif (j == 2): p = "o"
				print(p, end="")
			print()


	def input(self, p, x, y):

		# Processing a new input

		self.board[y][x] = p
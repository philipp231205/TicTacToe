class Board():

	def __init__(self):
		self.board = []

		# Filling the board

		for i in range(3):
			self.board.append([0,0,0])


	def output(self):

		# Outputting the current board State

		for i in self.board:
			for j in i:
				print(j, end="")
			print()
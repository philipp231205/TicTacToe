import copy
import win_verification as w

class AI():
	"""
	Class to calculate the best possible move
	"""

	def __init__(self):
		pass

	def turn(self, board, turn): # Returns coordinates for best possible move
		"""
		Returns coordinates for best possible move.

		Loops over all moves and scores them with score(), then returns best possible.
		"""

		best_score = None
		x = None
		y = None

		for i in range(3):
			for j in range(3):

				if (board[i][j] == 0): # Loops through every possible move for AI

					b = copy.deepcopy(board)

					b[i][j] = 2

					s = self.score(b, turn + 1, 1) # Scores the move

					# Stores the coordinates of the best move
					if (best_score == None):
						best_score = s
						x = j
						y = i
					elif (best_score < s):
						best_score = s
						x = j
						y = i

		return x,y
		

	def score(self, board, turn, p):
		"""
		Returns the score for a board state.

		If AI or player wins, return 10 or -10, with turn weighted in.

		Else it runs through all possible moves, and picks the best one of it.

		While looping through all, it finds the best possible move for the other player, which is expected to come.
		"""

		if w.Win_verification.v(board, 2): return 10 - (turn -1) # If AI wins, return score of 10 (including how deep the win was)
		elif w.Win_verification.v(board, 1): return (turn - 1) - 10 # If Player wins, return score of - 10 (including how deep the loss was)

		best_score = None
		opponent = 1 if p == 2 else 2

		for i in range(3):
			for j in range(3):

				if (board[i][j] == 0): # Loop through every possible move

					b = copy.deepcopy(board)
					b[i][j] = p

					s = self.score(b, turn + 1, opponent) # Find the best move for the opponent that is expected

					# Find the best move for AI or worst move for AI, depending on whose turn it is
					if (best_score == None): best_score = s
					elif (best_score < s and p == 2): best_score = s
					elif (best_score > s and p == 1): best_score = s

		if (best_score == None): return 0
		else: return best_score
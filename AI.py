import copy

class AI():

	def __init__(self):
		pass

	def turn(self, board, turn, p):

		# Calculating the next move for AI

		score = 0
		x = 0
		y = 0

		for i in range(3):
			for j in range(3):

				if (board[i][j] == 0):

					b = copy.deepcopy(board)
					b[i][j] = 2

					if self.win_verification(b, 2): s = 10000 ** (9 - turn)
					else:

						s = self.score(b, turn+1, 1)


					if (s > score or score == 0):
						score = s
						x = j
						y = i

		return x, y

	def score(self, board, turn, p):

		score = 0 # Score gets calculated based on how many options to win or to loose

		if turn == 9: # Last turn
			b = copy.deepcopy(board)

			if self.win_verification(b, 2): score += 11
			elif self.win_verification(b, 1): score -= 10

		else:
			for i in range(3):
				for j in range(3):

					b = copy.deepcopy(board)

					if (p == 2):

						if b[i][j] == 0:

							b[i][j] = 2

							if self.win_verification(b, 2): return 100 ** (9 - turn)
							else:
								score += self.score(b, turn + 1, 1)

					elif (p == 1):
						if b[i][j] == 0:
						
							b[i][j] = 1

							if self.win_verification(b, 1): return -(100 ** (9 - turn))
							else:

								score += self.score(b, turn + 1, 2)

		return score

	
	def win_verification(self, board, p):
			b = board
	
			if (b[0][0] == p and b[0][1] == p and b[0][2] == p): return True
			if (b[1][0] == p and b[1][1] == p and b[1][2] == p): return True
			if (b[2][0] == p and b[2][1] == p and b[2][2] == p): return True
	
			if (b[0][0] == p and b[1][0] == p and b[2][0] == p): return True
			if (b[0][1] == p and b[1][1] == p and b[2][1] == p): return True
			if (b[0][2] == p and b[1][2] == p and b[2][2] == p): return True
	
			if (b[0][0] == p and b[1][1] == p and b[2][2] == p): return True
			if (b[2][0] == p and b[1][1] == p and b[0][2] == p): return True
	
			return False


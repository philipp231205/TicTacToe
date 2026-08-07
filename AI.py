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

					s = self.score(b, turn+1, 1)


					if (s > score):
						score = s
						x = j
						y = i

						#print("x: " + str(x) + "y: " + str(y))

					#print(score)

		return x, y

	def score(self, board, turn, p):

		score = 0

		#print("Turn: " + str(turn))

		if turn == 8:
			for i in range(3):
				for j in range(3):
					b = copy.deepcopy(board)
					if b[i][j] == 0:

						b[i][j] = 2
						if self.win_verification(b, 2): score += 10
						if self.win_verification(b, 1): score -= 10

		else:
			for i in range(3):
				for j in range(3):

					b = copy.deepcopy(board)

					if (p == 2):

						if b[i][j] == 0:

							b[i][j] = 2

							if self.win_verification(b, 2): score += 10
							else:
								score += self.score(b, turn + 1, 1)

					else:
						if b[i][j] == 0:
						
							b[i][j] = 1

							if self.win_verification(b, 2): score -= 10
							else:

								score += self.score(b, turn + 1, 2)

		#print("Depth:" + str(turn) + ", Score: " + str(score))
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


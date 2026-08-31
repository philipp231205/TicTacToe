import copy

class AI():

	def __init__(self):
		pass

	def turn(self, board, turn, p):

		best_score = None
		x = None
		y = None

		for i in range(3):
			for j in range(3):

				if (board[i][j] == 0):

					b = copy.deepcopy(board)

					b[i][j] = 2

					s = self.score(b, turn + 1, 1)

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

		if self.win_verification(board, 2): return 10 - (turn -1)
		elif self.win_verification(board, 1): return (turn - 1) - 10

		best_score = None
		opponent = 1 if p == 2 else 2

		for i in range(3):
			for j in range(3):

				if (board[i][j] == 0):

					b = copy.deepcopy(board)
					b[i][j] = p

					s = self.score(b, turn + 1, opponent)

					if (best_score == None): best_score = s
					elif (best_score < s and p == 2): best_score = s
					elif (best_score > s and p == 1): best_score = s

		if (best_score == None): return 0
		else: return best_score
	
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

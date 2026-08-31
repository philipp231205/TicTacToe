import copy

class AI():

	def __init__(self):
		pass

	def turn(self, board, turn, p):

		# Calculating the next move for AI

		best_score = None
		x = 0
		y = 0

		for i in range(3):
			for j in range(3):

				if (board[i][j] == 0):
					b = copy.deepcopy(board)
					b[i][j] = p

					opponent = 1 if p == 2 else 2
					s = self.score(b, turn + 1, opponent)

					if best_score is None:
						best_score = s
						x = j
						y = i
					elif p == 2 and s > best_score:
						best_score = s
						x = j
						y = i
					elif p == 1 and s < best_score:
						best_score = s
						x = j
						y = i

		return x, y

	def score(self, board, turn, p):

		# Terminal positions: AI win, player win, or draw
		if self.win_verification(board, 2):
			return 10 - (turn - 1)
		if self.win_verification(board, 1):
			return (turn - 1) - 10

		moves = []
		for i in range(3):
			for j in range(3):
				if board[i][j] == 0:
					moves.append((i, j))

		if not moves:
			return 0

		best_score = None
		opponent = 1 if p == 2 else 2

		for i, j in moves:
			board[i][j] = p
			s = self.score(board, turn + 1, opponent)
			board[i][j] = 0

			if best_score is None:
				best_score = s
			elif p == 2 and s > best_score:
				best_score = s
			elif p == 1 and s < best_score:
				best_score = s

		return best_score

	
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

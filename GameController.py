import board
import AI

import copy

class GameController():

	def __init__(self):

		self.board_game = board.Board()
		self.ai = AI.AI()
		self.turn = 0

	def mainGameLoop(self):

		print("Player 1 begins \n")

		game_over = False
		winner = ""

		while (not game_over):
			self.board_game.output()

			self.turn += 1

			print()

			x = int(input("x: "))
			y = int(input("y: "))

			self.board_game.input(1, x, y)

			if self.win_verification(1):
				game_over = True
				winner = "Player 1"
			else:
				

				x, y = self.ai.turn(copy.deepcopy(self.board_game.get_board()), self.turn, 2)
				self.board_game.input(2, x, y)

				self.turn += 1

				if self.win_verification(2):
					game_over = True
					winner = "AI"

		print(winner + " wins!")

		self.board_game.output()

		return

	

	def win_verification(self, p):
		b = self.board_game.get_board()

		if (b[0][0] == p and b[0][1] == p and b[0][2] == p): return True
		if (b[1][0] == p and b[1][1] == p and b[1][2] == p): return True
		if (b[2][0] == p and b[2][1] == p and b[2][2] == p): return True

		if (b[0][0] == p and b[1][0] == p and b[2][0] == p): return True
		if (b[0][1] == p and b[1][1] == p and b[2][1] == p): return True
		if (b[0][2] == p and b[1][2] == p and b[2][2] == p): return True

		if (b[0][0] == p and b[1][1] == p and b[2][2] == p): return True
		if (b[2][0] == p and b[1][1] == p and b[0][2] == p): return True

		return False
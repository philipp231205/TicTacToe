import board
import AI

import copy

class GameController():

	def __init__(self, player):

		self.board_game = board.Board() # Initializes a new board
		self.ai = AI.AI() # Initializes the game Algorithm
		self.turn = 1 # Sets the turn count to 1
		self.player = player # Sets if the player or the AI is first

	def mainGameLoop(self):

		if (self.player == 1): print("Player starts")
		elif (self.player == 2): print("AI starts")

		game_over = False
		winner = ""

		while (not game_over):

			if (self.player == 1):
				self.board_game.output()
				
				print()

				x = int(input("x: "))
				y = int(input("y: "))

				print()

				self.board_game.input(1, x, y)
				self.player = 2

			elif (self.player == 2):
				x, y = self.ai.turn(copy.deepcopy(self.board_game.get_board()), self.turn, 2)
				self.board_game.input(2, x, y)

				self.player = 1

			if self.win_verification(1):
				game_over = True
				winner = "Player"

			elif self.win_verification(2):
				game_over = True
				winner = "AI"

			elif (self.turn == 9):
				game_over = True
				winner = "No one"

			self.turn += 1

		print(winner + " wins!")

		self.board_game.output()

		return

	

	def win_verification(self, p): # Rework necessary
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
import board
import AI
import win_verification as w

import copy

class GameController():
	"""
	Handles the Game.

	Controls turns and checks for win states.
	"""

	def __init__(self, player):

		"""
		Sets up the game state.
		"""

		self.board_game = board.Board() # Initializes a new board
		self.ai = AI.AI() # Initializes the game Algorithm
		self.turn = 1 # Sets the turn count to 1
		self.player = player # Sets if the player or the AI is first

	def mainGameLoop(self):
		"""
		Loops until a winner is found or it's a draw.

		One loop is one turn, with either player or AI moving.
		"""

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
				x, y = self.ai.turn(copy.deepcopy(self.board_game.get_board()), self.turn)
				self.board_game.input(2, x, y)

				self.player = 1

			if w.Win_verification.v(self.board_game.get_board(), 1):
				game_over = True
				winner = "Player"

			elif w.Win_verification.v(self.board_game.get_board(), 2):
				game_over = True
				winner = "AI"

			elif (self.turn == 9):
				game_over = True
				winner = "No one"

			self.turn += 1

		print(winner + " wins!")

		self.board_game.output()

		return
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
		self.turn = 1 # Sets the turn count to 1 as game starts here
		self.player = player # Sets if the player or the AI is first, by default 1 if not specificed through args

	def mainGameLoop(self):
		"""
		Loops until a winner is found or it's a draw.

		One loop is one turn, with either player or AI moving.
		"""

		if (self.player == 1): print("Player starts") # Prints information on who starts
		elif (self.player == 2): print("AI starts")

		game_over = False # Initializes loop requirement, once this is true, loop ends
		winner = "" # Winner string

		while (not game_over):

			if (self.player == 1): # If its players turn
				self.board_game.output() # Print the board
				
				print()

				x = int(input("x: "))
				y = int(input("y: ")) # Takes the x and y coordinates of where to place the players piece

				print()

				self.board_game.input(1, x, y)
				self.player = 2 # now it is the turn of algorithm

			elif (self.player == 2): # If its algorithms turn
				x, y = self.ai.turn(copy.deepcopy(self.board_game.get_board()), self.turn) # Calls the minimax algorithm to return best coordinates
				self.board_game.input(2, x, y)

				self.player = 1 # now its players turn

			if w.Win_verification.v(self.board_game.get_board(), 1): # Check if player has won
				game_over = True
				winner = "Player"

			elif w.Win_verification.v(self.board_game.get_board(), 2): # Check if algorithm has won
				game_over = True
				winner = "AI"

			elif (self.turn == 9): # If turn is 9, and no winner has been found, its a draw
				game_over = True
				winner = "No one"

			self.turn += 1

		print(winner + " wins!") # Print the player

		self.board_game.output() # Output the final state

		return
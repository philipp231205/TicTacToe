import board

class GameController():

	def __init__(self):

		self.board_game = board.Board()

	def mainGameLoop(self):

		print("Player 1 begins \n")

		game_over = False
		winner = ""

		while (not game_over):
			self.board_game.output()

			print()

			x = int(input("x: "))
			y = int(input("y: "))

			self.board_game.input(1, x, y)

			if self.win_verification(1):
				game_over = True
				winner = "Player 1"
			else:


				# KI Kalkulation hier

				if self.win_verification(2):
					game_over = True
					winner = "AI"

		print(winner + " wins!")

		return

	def win_verification(self, p):

		return True
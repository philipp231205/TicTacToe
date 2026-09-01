import GameController
import argparse

def main():
	"""
	Starts the TicTacToe Game.

	Parses player argument and then starts the game.
	"""

	parser = argparse.ArgumentParser()

	parser.add_argument( # Parses if player starts or not, 1 = player starts, 2 = algorithm starst
		"-p",
		"--player",
		type = int,
		default = 1
	)

	args = parser.parse_args()

	game_controller = GameController.GameController(args.player) # initialzies the game loop

	game_controller.mainGameLoop() # Starts the game

if __name__ == "__main__":
	main()
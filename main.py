import GameController
import argparse

def main(): 

	parser = argparse.ArgumentParser()

	parser.add_argument( # Parses if player starts or not
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
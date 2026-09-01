import board as b
import AI as a
import copy
import win_verification as w

def test():
    """
    Starts the test run and prints final result.
    """

    # Sets up a board an algorithm
    board = b.Board()
    ai = a.AI()

    # Runs the test
    results = run_test(board.get_board(), 1)

    print("Final result: " + str(results[0]) + " wins, " + str(results[1]) + " draws, " + str(results[2]) + " losses") # Final output


def run_test(board, turn):
    """
    Given player starts, runs through every possible move player can make.

    Stores amount the game results in AI win, draw or Player win.
    """
    results = [0,0,0] # AI wins, draws, Player wins

    for i in range(3):
        for j in range(3):
            if (board[i][j] == 0): # Runs through all possible moves
                b = copy.deepcopy(board)
                b[i][j] = 1

                if w.Win_verification.v(b, 1): results[2] += 1
                elif (turn == 9): results[1] += 1
                else:

                    x,y = a.AI().turn(board, turn+1)

                    b[i][j] = 2

                    if w.Win_verification.v(b, 2): results[0] += 1
                    else:

                        r = run_test(b, turn+2)

                        results[0] += r[0]
                        results[1] += r[1]
                        results[2] += r[2]

    return results

test()
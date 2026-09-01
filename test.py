import board as b
import AI as a
import copy
import win_verification as w

def test():
    """
    Starts the test run and prints final result.
    """

    # Sets up a board
    board = b.Board()

    # Runs the test
    results_p1 = run_test_p1(board.get_board(), 1)

    print("Final result: " + str(results_p1[0]) + " wins, " + str(results_p1[1]) + " draws, " + str(results_p1[2]) + " losses when Player starts") # Final output

    results_p2 = run_test_p2(board.get_board(), 1)
    
    print("Final result: " + str(results_p2[0]) + " wins, " + str(results_p2[1]) + " draws, " + str(results_p2[2]) + " losses when Algorithm starts") # Final output

def run_test_p1(board, turn):
    """
    Given player starts, runs through every possible move player can make.

    Stores amount the game results in AI win, draw or Player win.
    """
    results = [0,0,0] # AI wins, draws, Player wins

    for i in range(3):
        for j in range(3):
            if (board[i][j] == 0): # Runs through all possible moves
                b = copy.deepcopy(board)
                b[i][j] = 1 # Simulates all possible player moves

                if w.Win_verification().v(b, 1): results[2] += 1 # If player wins
                elif (turn >= 9): results[1] += 1 # If all places full
                else:

                    x,y = a.AI().turn(b, turn+1) # Simulate algorithm turn

                    b[y][x] = 2

                    if w.Win_verification().v(b, 2): results[0] += 1 # If AI wins
                    else:

                        r = run_test_p1(b, turn+2) # Recursive test run

                        results[0] += r[0] # Summing of the scores
                        results[1] += r[1]
                        results[2] += r[2]

    return results

def run_test_p2(board, turn):
    """
    Given algorithm starts, runs through every possible move player can make.

    Stores amount the game results in AI win, draw or Player win.
    """
    results = [0,0,0] # AI wins, draws, Player wins

    x,y = a.AI().turn(board, turn) # First runs the algorithm
    board[y][x] = 2

    if w.Win_verification().v(board, 2): results[0] += 1 # Checks if algorithm has won
    elif (turn >= 9): results[1] += 1 # Checks if its a draw
    else: # Else simulates all poosible following player moves

        for i in range(3):
            for j in range(3):

                if (board[i][j] == 0):

                    b = copy.deepcopy(board)

                    b[i][j] = 1 # Simulation of all player moves

                    if w.Win_verification().v(b, 1): results[2] += 1 # If player won
                    else:

                        r = run_test_p2(b, turn + 2) # Recursive test run

                        results[0] += r[0] # Summing of all results
                        results[1] += r[1]
                        results[2] += r[2]

    return results

test()
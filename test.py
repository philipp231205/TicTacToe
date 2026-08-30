import board as b
import AI as a
import copy

def test():

    board = b.Board()
    ai = a.AI()

    results = run_test(board.get_board(), 1)

    print("Final result: " + str(results[0]) + " wins, " + str(results[1]) + " draws, " + str(results[2]) + " losses")


def run_test(board, turn):
    results = [0,0,0] # AI wins, draws, Player wins

    for i in range(3):
        for j in range(3):
            if (board[i][j] == 0):
                b = copy.deepcopy(board)
                b[i][j] = 1

                if win_verification(b, 1): results[2] += 1
                elif (turn == 9): results[1] += 1
                else:

                    x,y = a.AI().turn(board, turn+1, 2)

                    b[i][j] = 2

                    if win_verification(b, 2): results[0] += 1
                    else:

                        r = run_test(b, turn+2)

                        results[0] += r[0]
                        results[1] += r[1]
                        results[2] += r[2]

    return results

def win_verification(b, p): # Rework necessary

    if (b[0][0] == p and b[0][1] == p and b[0][2] == p): return True
    if (b[1][0] == p and b[1][1] == p and b[1][2] == p): return True
    if (b[2][0] == p and b[2][1] == p and b[2][2] == p): return True

    if (b[0][0] == p and b[1][0] == p and b[2][0] == p): return True
    if (b[0][1] == p and b[1][1] == p and b[2][1] == p): return True
    if (b[0][2] == p and b[1][2] == p and b[2][2] == p): return True

    if (b[0][0] == p and b[1][1] == p and b[2][2] == p): return True
    if (b[2][0] == p and b[1][1] == p and b[0][2] == p): return True

    return False


test()
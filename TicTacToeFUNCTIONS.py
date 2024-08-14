#################VISUALS########################
intro = ("Welcome to TicTacToe!"
         "  PLAYER1(X) PLAYER2(O)")

board = [
    [["_"], ["_"], ["_"]],
    [["_"], ["_"], ["_"]],
    [["_"], ["_"], ["_"]]
]

moves = ["X", "O"]


#############FUNCTIONS################


def display():
    for row in board:
        print(row)


def check_row_win(active_board):
    for row in active_board:
        sequential_plays_x = 0
        sequential_plays_o = 0
        for play in row:
            if play[0] == "X":
                sequential_plays_x += 1
            elif play[0] == "O":
                sequential_plays_o += 1

            if sequential_plays_x == 3:
                print("PLAYER1 WINS!")
                return True
            elif sequential_plays_o == 3:
                print("PLAYER2 WINS!")
                return True
    return False


def check_column_win(active_board):
    column_index = {0, 1, 2}
    for column in column_index:
        sequential_plays_x = 0
        sequential_plays_o = 0
        for row in active_board:
            if row[column][0] == "X":
                sequential_plays_x += 1
            elif row[column][0] == "O":
                sequential_plays_o += 1
        if sequential_plays_x == 3:
            print("PLAYER1 WINS!")
            return True
        elif sequential_plays_o == 3:
            print("PLAYER2 WINS!")
            return True
    return False


def check_diagonal_win(active_board):
    players = {"X": "PLAYER1",
               "O": "PLAYER2"}
    middle_play = active_board[1][1][0]
    top_left_c = active_board[0][0][0]
    bottom_right_c = active_board[2][2][0]
    top_right_c = active_board[0][2][0]
    bottom_left_c = active_board[2][0][0]
    if middle_play != "_":
        if top_left_c == middle_play and bottom_right_c == middle_play:
            print(f"{players[middle_play]} WINS!")
            return True
        elif top_right_c == middle_play and bottom_left_c == middle_play:
            print(f"{players[middle_play]} WINS!")
            return True
    return False


def check_tie(active_board):
    for row in active_board:
        if "_" in [x[0] for x in row]:
            return False
    print("TIE")
    return True


def check_for_win(active_board):
    if check_row_win(active_board):
        return True
    elif check_column_win(active_board):
        return True
    elif check_diagonal_win(active_board):
        return True
    elif check_tie(active_board):
        return True
    else:
        return False

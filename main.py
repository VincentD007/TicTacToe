from TicTacToeFUNCTIONS import display, intro, check_for_win

board = [
    [["_"], ["_"], ["_"]],
    [["_"], ["_"], ["_"]],
    [["_"], ["_"], ["_"]]
]


print(intro)
display(board)


def update_board(move, player_icon, active_board):
    if len(move) > 2 or len(move) < 2:
        print("Not a valid move! Try again.")
        return False
    else:
        for value in move:
            if value not in [str(num) for num in range(11)]:
                print("Not a valid move! Try again.")
                return False
    row = int(move[0]) - 1
    column = int(move[1]) - 1
    if active_board[row][column][0] == "_":
        active_board[row][column][0] = player_icon
        return True
    else:
        print("That play has been made!")
        return False


play_game = True
player_turn = 1

while play_game:
    if player_turn == 1:
        player1move = input("PLAYER1(X) Move: ")
        open_spot = update_board(player1move, "X", board)
        display(board)
        if open_spot:
            player_turn = 2
            if check_for_win(board):
                play_game = False
    elif player_turn == 2:
        player2move = input("PLAYER2(O) Move: ")
        open_spot = update_board(player2move, "O", board)
        display(board)
        if open_spot:
            player_turn = 1
            if check_for_win(board):
                play_game = False

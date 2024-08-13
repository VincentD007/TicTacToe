from TicTacToeFUNCTIONS import display, intro, check_for_win, board

print(intro)
display()


def update_board(move, player_icon):
    row = int(move[0]) - 1
    column = int(move[1]) - 1
    if board[row][column][0] == "_":
        board[row][column][0] = player_icon
        return True
    else:
        print("That play has been made!")
        return False


play_game = True
player_turn = 1

while play_game:
    if player_turn == 1:
        player1move = input("PLAYER1(X) Move: ")
        open_spot = update_board(player1move, "X")
        display()
        player_turn = 2
        if check_for_win(board):
            play_game = False
    elif player_turn == 2:
        player2move = input("PLAYER2(O) Move: ")
        open_spot = update_board(player2move, "O")
        display()
        player_turn = 1
        if check_for_win(board):
            play_game = False

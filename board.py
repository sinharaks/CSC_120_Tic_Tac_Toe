# Python Program for simple Tic Tac Toe

board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

game_still_going = True
winner = None
current_player = "Player 1"
current_player_tic_pick = "X"

def play_game():
    print_board()

    while game_still_going:
        handle_turn(current_player)
        flip_player()

def print_board():
    print("Printing board")
    print("['" + board[0][0] + "', '" + board[0][1] + "', '" + board[0][2] + "']")
    print("['" + board[1][0] + "', '" + board[1][1] + "', '" + board[1][2] + "']")
    print("['" + board[2][0] + "', '" + board[2][1] + "', '" + board[2][2] + "']")
    print("\n")

def isvalidinput(rowposition, colposition):
    if(int(rowposition) >= 0 and int(rowposition) < 3 and int(colposition) >= 0 and int(colposition) < 3):
        return True
    else:
        return False

def ispositionavailableinboard(rowposition, colposition):
    if (board[rowposition][colposition] == "-"):
        return True
    else:
        return False

def handle_turn(player):
    print(player + ", make your move")
    rowposition = int(input("Enter row nos (0-2):"))
    colposition = int(input("Enter col nos (0-2):"))

    if(isvalidinput(rowposition, colposition)):
        if(ispositionavailableinboard(rowposition, colposition)):
            valid = False
        else:
            print("\n**** Board["+str(rowposition)+"]["+str(colposition)+"] has already been selected. Please somewhere else on the board ****")
            print("**** Invalid choice. Please mark again! ****")
            print_board()
            handle_turn(player)
    else:
        print("\n**** Invalid row or column: Please select row / col between 0 to 2 ****")
        print("**** Invalid choice. Please mark again! ****")
        print_board()
        handle_turn(player)

    print("\n" + player + " added mark at the location " + str(rowposition) + "," + str(colposition))
    board[rowposition][colposition] = current_player_tic_pick
    print_board()

def check_rows():
    global game_still_going
    row_1 = board[0][0] == board[0][1] == board[0][2] != "-"
    row_2 = board[1][0] == board[1][1] == board[1][2] != "-"
    row_3 = board[2][0] == board[2][1] == board[2][2] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0][0]
    elif row_2:
        return board[1][0]
    elif row_3:
        return board[2][0]
    else:
        return None

def check_columns():
    global game_still_going
    column_1 = board[0][0] == board[1][0] == board[2][0] != "-"
    column_2 = board[0][1] == board[1][1] == board[2][1] != "-"
    column_3 = board[0][2] == board[1][2] == board[2][2] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0][0]
    elif column_2:
        return board[1][0]
    elif column_3:
        return board[2][0]
    else:
        return None

def check_diagonals():
    global game_still_going
    diagonal_1 = board[0][0] == board[1][1] == board[2][2] != "-"
    diagonal_2 = board[2][0] == board[1][1] == board[0][2] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0][0]
    elif diagonal_2:
       return board[2][0]
    else:
        return None

def flip_player():
    global current_player
    global current_player_tic_pick

    if current_player_tic_pick == "X":
        current_player = "Player 2"
        current_player_tic_pick = "O"
    elif current_player_tic_pick == "O":
        current_player = "Player 1"
        current_player_tic_pick = "X"

play_game()
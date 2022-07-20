#!/usr/bin/python
import sqlite3

game_still_going = True
winner = None
current_player = "Player1"
firstPlayerId = 1
secondPlayerId = 2
current_player_tic_pick = "X"
gameId = 0

def getGameId():
    conn = sqlite3.connect('C:\CSC120\CSC_120_demo\CSC_120_Tic_Tac_Toe\game.db')

    print("Opened database successfully");
    cursor = conn.execute("SELECT MAX(gameid) from game")

    for row in cursor:
        gameId = row[0]

    if(gameId is None):
        gameId = 1
    else:
        gameId = int(gameId) + 1

    print("Operation done successfully");
    conn.close()

    return gameId

def addGameInfo(firstPlayerId, secondPlayerId, gamestatus, winnerId):
    conn = sqlite3.connect('C:\CSC120\CSC_120_demo\CSC_120_Tic_Tac_Toe\game.db')
    gameId = getGameId()
    print("Opened database successfully");

    insertQuery = "INSERT INTO GAME (gameid, firstPlayerId, secondPlayerId, gamestatus, winnerid) VALUES (" + str(gameId)+"," + str(firstPlayerId) +"," + str(secondPlayerId) +",'" + gamestatus + "'," + str(winnerId)+");"

    print(insertQuery)
    cursor = conn.execute(insertQuery)
    conn.commit()
    print("Operation done successfully")
    conn.close()

# Python Program for Tic Tac Toe Game
# Declare a list of lists
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

# Function for Tic Tac Toe Game play
def play_game():
    print_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X":
        print("Player1 wins!. Game over!")
        addGameInfo(firstPlayerId, secondPlayerId, 'W', firstPlayerId)
    elif winner == "O":
        print("Players2 wins!. Game over!")
        addGameInfo(firstPlayerId, secondPlayerId, 'W', secondPlayerId)
    elif winner is None:
        print("it's a Tie!. Game draw!")
        addGameInfo(firstPlayerId, secondPlayerId, 'D', 0)

# prints the current board
def print_board():
    print("Printing board")
    print("['" + board[0][0] + "', '" + board[0][1] + "', '" + board[0][2] + "']")
    print("['" + board[1][0] + "', '" + board[1][1] + "', '" + board[1][2] + "']")
    print("['" + board[2][0] + "', '" + board[2][1] + "', '" + board[2][2] + "']")
    print("\n")

# checks if input is valid
# Valid: if row number is between 0 and 2 and column number is also between 0 and 2
def isvalidinput(rowposition, colposition):
    if(int(rowposition) >= 0 and int(rowposition) < 3 and int(colposition) >= 0 and int(colposition) < 3):
        return True
    else:
        return False

# checks if row and column position is available
def ispositionavailableinboard(rowposition, colposition):
    if (board[rowposition][colposition] == "-"):
        return True
    else:
        return False

# function that handles players turn
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

# Checks if the game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()

# Checks if there is a winner
def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

# checks if the row has an empty data
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

# checks if the column has an empty data
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

# checks if the diagonal has an empty data
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

# checks if there is a tie
def check_for_tie():
    global game_still_going
    if ("-" in board[0][0] or "-" in board[0][1] or "-" in board[0][2] or "-" in board[1][0] or "-" in board[1][1]
            or "-" in board[1][2] or "-" in board[2][0] or "-" in board[2][1] or "-" in board[2][2]):
        return False
    else:
        game_still_going = False
        return True

# Flips player from 1 to 2 or vice versa
def flip_player():
    global current_player
    global current_player_tic_pick

    if current_player_tic_pick == "X":
        current_player = "Player 2"
        current_player_tic_pick = "O"
    elif current_player_tic_pick == "O":
        current_player = "Player 1"
        current_player_tic_pick = "X"

# call madse to play Tic Tac Toe game
play_game()
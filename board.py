# Python Program for simple Tic Tac Toe
# declare a board in terms of a list object
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# function to display initial Tic-Tac-Toe board
def display_board():
    print("\n")
    print("['"+ board[0] + "', '" + board[1] + "', '" + board[2] + "']")
    print("['"+ board[3] + "', '" + board[4] + "', '" + board[5] + "']")
    print("['"+ board[6] + "', '" + board[7] + "', '" + board[8] + "']")
    print("\n")

display_board()
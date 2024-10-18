# Tic Tac Toe Game in Python

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Function to get player input and make a move
def player_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row and column 1-3): ").split())
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid input, please enter row and column numbers between 1 and 3.")
                continue
            if board[row - 1][col - 1] == " ":
                board[row - 1][col - 1] = player
                break
            else:
                print("Cell already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter valid numbers for row and column (1-3).")

# Main game function
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player_move(board, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()

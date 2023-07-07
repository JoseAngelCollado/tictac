board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board():
    for row in board:
        print("|" + "|".join(row) + "|")

def make_move(player):
    x = int(input(f"Player {player}, enter x coordinate: "))
    y = int(input(f"Player {player}, enter y coordinate: "))
    if board[y][x] != " ":
        print("Invalid move, try again")
        return make_move(player)
    board[y][x] = player

def has_winner():
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    # no winner
    return None

def play_game():
    player = "X"
    while True:
        print_board()
        make_move(player)
        winner = has_winner()
        if winner:
            print_board()
            print(f"{winner} wins!")
            break
        player = "X" if player == "O" else "O"

play_game()
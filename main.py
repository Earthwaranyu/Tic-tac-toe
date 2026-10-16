from game import create_board, has_won, is_draw, is_valid_move, place_symbol


def display_board(board):
    rows = (board[0:3], board[3:6], board[6:9])
    for row_number, row in enumerate(rows):
        print(" | ".join(row))
        if row_number < 2:
            print("---------")


def read_square(player):
    while True:
        try:
            square = int(input(f"Player {player}, choose a square (1-9): "))
        except ValueError:
            print("Error: input must be a number from 1-9.")
            continue
        if not 1 <= square <= 9:
            print("Error: input can only be 1-9.")
            continue
        return square


def play_game():
    board = create_board()
    player = "X"

    while True:
        display_board(board)
        square = read_square(player)

        if not is_valid_move(board, square):
            print("Error: that square is already occupied.")
            continue

        place_symbol(board, square, player)
        if has_won(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            return
        if is_draw(board):
            display_board(board)
            print("The game is a draw.")
            return

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    play_game()
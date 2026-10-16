BOARD_SIZE = 9
SYMBOLS = ("X", "O")
WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def create_board():
    return [" "] * BOARD_SIZE


def is_valid_move(board, square):
    return 1 <= square <= BOARD_SIZE and board[square - 1] == " "


def place_symbol(board, square, symbol):
    if symbol not in SYMBOLS:
        raise ValueError("Symbol must be X or O")
    if not is_valid_move(board, square):
        raise ValueError("Square must be an unoccupied number from 1 to 9")
    board[square - 1] = symbol


def has_won(board, symbol):
    return any(all(board[index] == symbol for index in line) for line in WINNING_LINES)


def is_draw(board):
    return all(square != " " for square in board) and not any(
        has_won(board, symbol) for symbol in SYMBOLS
    )
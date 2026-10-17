from game import create_board, has_won, is_draw, is_valid_move, place_symbol


def test_c1_x_wins_after_entering_square_three():
    board = create_board()
    place_symbol(board, 1, "X")
    place_symbol(board, 2, "X")
    place_symbol(board, 4, "O")
    place_symbol(board, 5, "O")

    assert is_valid_move(board, 3)
    place_symbol(board, 3, "X")

    assert has_won(board, "X")


def test_c2_square_ten_is_invalid():
    board = create_board()

    assert not is_valid_move(board, 10)


def test_c3_occupied_square_is_invalid_and_board_is_unchanged():
    board = create_board()
    place_symbol(board, 5, "X")
    board_before_invalid_move = board.copy()

    assert not is_valid_move(board, 5)

    try:
        place_symbol(board, 5, "O")
    except ValueError:
        pass

    assert board == board_before_invalid_move


def test_c5_full_board_without_winner_is_a_draw():
    board = create_board()
    moves = ((1, "X"), (2, "O"), (3, "X"), (5, "O"), (4, "X"),
             (6, "O"), (8, "X"), (7, "O"), (9, "X"))

    for square, symbol in moves:
        place_symbol(board, square, symbol)

    assert is_draw(board)
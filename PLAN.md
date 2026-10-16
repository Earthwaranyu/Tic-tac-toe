# Implementation plan

1. Create `game.py` for the board, player symbols, move validation, symbol placement, win detection, and draw detection. Keep all game rules as **plain functions**.

2. Create `main.py` for displaying the board, reading player input, reporting errors, and controlling alternating turns.

3. Handle occupied squares and invalid selections in `game.py`, ensuring only squares **1–9** can be played and existing moves **cannot be replaced**.

4. Convert the checks in `EVIDENCE.md` into automated **pytest** cases:
   - Verify X wins with squares `1`, `2`, `3`
   - Verify input `10` is rejected

   Run them with:
```bash
   uv run pytest
```

5. Run the game and play one complete game, including an invalid or occupied-square attempt, to judge whether the game works for two local players:
```bash
   uv run main.py
```
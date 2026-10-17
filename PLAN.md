# Implementation plan

1. Create `game.py` for the board, player symbols, move validation, symbol placement, win detection, and draw detection. Keep all game rules as **plain functions**. (R1, R2, R5)

2. Create `main.py` for displaying the board, reading player input, reporting errors, and controlling alternating turns. (R1)

3. Handle occupied squares and invalid selections in `game.py`, ensuring only squares **1–9** can be played and existing moves **cannot be replaced**. (R3, R4)

4. Convert the checks in `EVIDENCE.md` into automated **pytest** cases:
   - Verify X wins with squares `1`, `2`, `3` (R2)
   - Verify input `10` is rejected (R4)

   Run them with:
```bash
   uv run pytest
```

5. Run the game and play one complete game, including an invalid or occupied-square attempt, to judge whether the game works for two local players:
```bash
   uv run main.py
```

## Later changes
- The two checks in step 4 were planned before implementing, but I only created EVIDENCE.md after game.py and main.py were committed. I added it afterwards and kept these expected results unchanged.
- I added pyproject.toml, uv.lock and pytest afterwards, because `uv sync` and `uv run pytest` did not work from a fresh copy without them.
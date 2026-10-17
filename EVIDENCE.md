# Checks and decisions

> This file records what I checked, what actually happened, and why I accepted or changed the work. It does not repeat setup instructions or the implementation plan.

## Concrete checks
Write the first two expectations before implementation. Fill in actual results after running them.

| Check / requirement | Given | When | Expected result | Actual result / pass or fail |
|---|---|---|---|---|
| C1 / R2 — normal case | New game; X has squares 1 and 2, O has 4 and 5; X to play | X enters 3 | "Player X wins!" is shown and the game ends | The board showed X on the top row, then "Player X wins!" was printed and the program ended. **Pass** |
| C2 / R4 — boundary or failure case | New game, X to play | X enters 10 | "Error: input can only be 1-9." and X is asked again | "Error: input can only be 1-9." was printed, the board stayed empty and "Player X, choose a square (1-9):" appeared again. **Pass** |
| C3 / R3 — invalid move | X has square 5, O to play | O enters 5 | "Error: that square is already occupied.", board unchanged, O is asked again | "Error: that square is already occupied." was printed, X stayed in square 5 and the prompt still said Player O. **Pass** |
| C4 / R1 — symbols and turns | New game | X enteres 1, then O enters 2 | X shows in sqaure 1, O in square 2, and the prompts go Player X then Player O | X appeared in square 1 (top-left) and O in square 2. The prompts went "Player X", then "Player O", then back to "Player X". **Pass** |
| C5 / R5 — draw | Moves 1,2,3,5,4,6,8,7 played (no three in a row) | X enteres 9 | Board is full, "The game is a draw." is shown and the game ends | The final board was X O X / X O O / O X X, then "The game is a draw." was printed and the program ended. **Pass** |



## Two review decisions
- Plan decision: 
I accepted Copilot's plan to keep all game rules in `game.py` and all input/output in `main.py`, because the tests can then call `has_won`, `is_valid_move` and `is_draw` directly without anyone typing. I kept Copilot away from writing EVIDENCE.md and from changing any expected results, because the checks and the judgment need to be my own work.
- Code decision: I accepted Copilot's C3 test in `tests/test_game.py` because it copies the board, tries to place O on the occupied square 5, and checks the board is unchanged. That matches my expected result "board unchanged", not just "the move is invalid".


## Automated tests
- Test file and behaviour checked: tests/test_game.py - X wins with 1, 2, 3 (C1); square 10 rejected (C2); occupied square rejected (C3); full board with no winner is a draw (C5).
- Command I ran: `uv run pytest`
- Final result: `collected 4 items and 4 passed in 0.00s`
- Correction and rerun, if needed: None needed. All 4 tests passed on the first run.

## Realistic use and final judgment
- Task I tried: Played a full game against a friend on my laptop. We also intentionally make mistake on some case like occupied square too see the output, and the output is as expected (Error: that square is already occupied.). 
- Outcome: It was playable and fun, the error messages are quite clear. The player was always asked again, so no turn was lost.
- Judgment: Done. All five manual checks (C1-C5) passed, covering R1-R5, all 4 automated tests pass, and a full game with a friend worked from started to finish.
- Remaining limitation or unfinished work: There is no bots to play with. The player need to restart the program if they want to play it again. The score is also not kept.
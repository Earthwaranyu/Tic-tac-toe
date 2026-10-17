# Checks and decisions

> This file records what I checked, what actually happened, and why I accepted or changed the work. It does not repeat setup instructions or the implementation plan.

## Concrete checks
Write the first two expectations before implementation. Fill in actual results after running them.

| Check / requirement | Given | When | Expected result | Actual result / pass or fail |
|---|---|---|---|---|
| C1 / R2 — normal case | New game; X has squares 1 and 2, O has 4 and 5; X to play | X enters 3 | "Player X wins!" is shown and the game ends | [Complete after checking.] |
| C2 / R4 — boundary or failure case | New game, X to play | X enters 10 | "Error: input can only be 1-9." and X is asked again | [Complete after checking.] |
| C3 / R3 — invalid move | X has square 5, O to play | O enters 5 | "Error: that square is already occupied.", board unchanged, O is asked again | [Complete after checking.] |
| C4 / R1 — symbols and turns | New game | X enteres 1, then O enters 2 | X shows in sqaure 1, O in square 2, and the prompts go Player X then Player O | [Complete after checking.] |
| C5 / R5 — draw | Moves 1,2,3,5,4,6,8,7 played (no three in a row) | X enteres 9 | Board is full, "The game is a draw." is shown and the game ends | [Complete after checking.] |



## Two review decisions
- Plan decision: 
I accepted to let Copilot implement and test the code because it can save so much time on writing the code. Copilot cannot change EVIDENCE.md because it needs to be my own work. 
- Code decision: [File/function/component, what I accepted or changed, and why. One or two sentences.]


## Automated tests
- Test file and behaviour checked: [...]
- Command I ran: [...]
- Final result: [Actual test count and outcome.]
- Correction and rerun, if needed: [Brief account, or None needed.]

## Realistic use and final judgment
- Task I tried: [One realistic use from start to finish.]
- Outcome: [What happened and whether it served the intended user/purpose.]
- Judgment: [Done / Partly done / Not done, with a brief reason based on the evidence.]
- Remaining limitation or unfinished work: [One specific item, or a useful next check.]
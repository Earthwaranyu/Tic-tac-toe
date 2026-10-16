# ❌⭕ Tic-Tac-Toe

> This file explains who the project is for, what it does, and how to run it.



##  Purpose

It is a 2 local players game. Normal casual people can play with each other for fun in their free time.



##  Requirements

| ID | Rule | Description |
|:--:|------|-------------|
| **R1** | Symbols & board | There are 2 symbols for this game, 1 player will get **X** symbol and 1 player will get **O** symbol. The square is **3x3**. |
| **R2** | Winning | Player can win by putting the **3 symbols in a row**, column, or diagonal. For example, putting **X** in square number **1, 2, and 3** to win. |
| **R3** | Occupied squares | If that square is occupied, **both player** can't put any symbol in it anymore. |
| **R4** | Valid input | The selected square cannot be less than 1 and more than 9. (Accepted input: 1-9) |
| **R5** | Draw | If all of the squares are occupied and there is no winner yet, the game is draw. |

---

##  Setup and Use

### Prerequisites

-  Python 3.12
-  uv

### Set up

```bash
uv sync
```

### Run 

```bash
uv run main.py
```

Then Player can start typing number from 1-9.

### Run the Tests

```bash
uv run pytest
```

---

##  Author and Acknowledgements

| | |
|---|---|
| **Name** | Waranyu Chunhachatcharachai |
| **Student ID** | 6681376 |
| **AI tools used** | GitHub Copilot in VS Code |
| **External code/resources** | None |

---

##  More Documentation

- See PLAN.md for the implementation plan and EVIDENCE.md for results and decisions.
def checkmate(board):
    if not isinstance(board, str) or board == "":
        print("Error")
        return

    grid = [row for row in board.split("\n") if row]
    n = len(grid)
    if n == 0:
        print("Error")
        return

    if any(len(row) != n for row in grid):
        print("Error")
        return

    kings = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == "K"]
    if len(kings) != 1:
        print("Error")
        return

    kr, kc = kings[0]
    valid_chars = set("KQBRP")

    # (direction, enemies_that_attack_from_here, can_slide_multiple_squares)
    attack_rules = [
        ((-1, -1), "BQ", True),
        ((-1, 1),  "BQ", True),
        ((1, -1),  "BQ", True),
        ((1, 1),   "BQ", True),
        ((-1, 0),  "RQ", True),
        ((1, 0),   "RQ", True),
        ((0, -1),  "RQ", True),
        ((0, 1),   "RQ", True),
        ((1, -1),  "P",  False),
        ((1, 1),   "P",  False),
    ]

    for (dr, dc), targets, sliding in attack_rules:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            square = grid[r][c]
            if square in targets:
                print("Success")
                return
            if square in valid_chars:
                break
            if not sliding:
                break
            r += dr
            c += dc

    print("Fail")
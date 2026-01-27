def solveNQueens(n):
    chessboard = [['.'] * n for _ in range(n)]
    answers = []

    cols = [-1] * n
    row = 0

    while row >= 0:
        # Remove previous queen in this row (important!)
        if cols[row] != -1:
            chessboard[row][cols[row]] = '.'

        placed = False
        start_col = cols[row] + 1

        for col in range(start_col, n):
            safe = True
            for r in range(row):
                if cols[r] == col or abs(cols[r] - col) == abs(r - row):
                    safe = False
                    break

            if safe:
                cols[row] = col
                chessboard[row][col] = 'Q'
                placed = True

                if row == n - 1:
                    answers.append([''.join(r) for r in chessboard])
                else:
                    row += 1
                    cols[row] = -1
                break

        if not placed:
            cols[row] = -1
            row -= 1

    return answers


solutions = solveNQueens(4)
print(solutions)

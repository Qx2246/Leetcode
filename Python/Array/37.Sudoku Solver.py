# Solution 1:
class Solution(object):
    def solveSudoku(self, board):
        n = 9

        def isValid(row, col, ch):
            for i in range(9):
                if board[i][col] == ch:
                    return False
                if board[row][i] == ch:
                    return False
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
                    return False
            return True

        def solve(row, col):
            if row == n:
                return True
            if col == n:
                return solve(row + 1, 0)

            if board[row][col] == ".":
                for i in range(1, 10):
                    if isValid(row, col, str(i)):
                        board[row][col] = str(i)
                        if solve(row, col + 1):
                            return True
                        board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)

        solve(0, 0)



# Solution 2:
class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize tracking sets and record empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(index):
            if index == len(empty_cells):
                return True  # All cells filled correctly

            r, c = empty_cells[index]
            b = (r // 3) * 3 + (c // 3)

            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack(index + 1):
                        return True

                    # Undo
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            return False  # No valid number worked

        backtrack(0)


# Solution 3:
class Solution:
    def solveSudoku(self, board):
        row = [[False]*9 for _ in range(9)]
        col = [[False]*9 for _ in range(9)]
        box = [[False]*9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    idx = int(board[r][c]) - 1
                    box_no = (r // 3) * 3 + (c // 3)
                    row[r][idx] = col[c][idx] = box[box_no][idx] = True

        def backtrack(r, c):
            if r == 9:
                return True

            next_r, next_c = (r + 1, 0) if c == 8 else (r, c + 1)

            if board[r][c] != '.':
                return backtrack(next_r, next_c)

            box_no = (r // 3) * 3 + (c // 3)
            for num in range(1, 10):
                idx = num - 1
                if not row[r][idx] and not col[c][idx] and not box[box_no][idx]:
                    board[r][c] = str(num)
                    row[r][idx] = col[c][idx] = box[box_no][idx] = True

                    if backtrack(next_r, next_c):
                        return True

                    board[r][c] = '.'
                    row[r][idx] = col[c][idx] = box[box_no][idx] = False

            return False

        backtrack(0, 0)

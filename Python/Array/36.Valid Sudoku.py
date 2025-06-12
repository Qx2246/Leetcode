# Solution 1: use set()
class Solution(object):
    def isValidSudoku(self, board):
        
        seen = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    row_key = (num, i)
                    col_key = (j, num)
                    box_key = (i//3, j//3, num)
                    if row_key in seen or col_key in seen or box_key in seen:
                        return False
                    seen.update([row_key, col_key, box_key])
        
        return True

# Solution 2: fasy way of using set()
def isValidSudoku(self, board):
    seen = sum(([(c, i), (j, c), (i//3, j//3, c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'), [])
    return len(seen) == len(set(seen))


#Solution 3: use any
def isValidSudoku(self, board):
    seen = set()
    return not any(x in seen or seen.add(x)
                   for i, row in enumerate(board)
                   for j, c in enumerate(row)
                   if c != '.'
                   for x in ((c, i), (j, c), (i/3, j/3, c)))

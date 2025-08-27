# Solution 1: [::-1] and zip Method
class Solution(object):
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])
    # zip: a function used to transpose the matrix --> e.g. zip(['a', 'b', 'c'], [1, 2, 3]) ==> ('a', 1) ('b', 2) ('c', 3)
    # * is the splat operator. It is used for unpacking a list into arguments. e.g. foo(*[1, 2, 3]) is the same as foo(1, 2, 3).

# Solution 1.1: by applying 'List'
class Solution(object):
    def rotate(self, matrix):
        matrix[:] = map(list, zip(*matrix[::-1]))

# Solution 3: 
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n/2):
            for j in range(n-n/2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                              matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

# Solution 3.1: List Comprehension
class Solution(object):
    def rotate(self, matrix):
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]


# Solution 4: Flip Flip (using 'reverse')
class Solution(object):
    def rotate(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range (i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

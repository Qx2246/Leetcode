class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]
        
'''
      ""  r   o   s
""    0   1   2   3
h     1   1   2   3
ho    2   2   1   2
hor   3   2   2   2
hors  4   3   3   2
horse 5   4   4   3

Replace → dp[i-1][j-1] + 1
Delete from word1 → dp[i-1][j] + 1
Insert into word1 → dp[i][j-1] + 1
'''

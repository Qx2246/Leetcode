# Solution 1: Dynamic Programming (bottom up)
class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1

        for i in range(n-1, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i+1]
                if i < n-1 and (s[i] == "1" or (s[i] == "2" and s[i+1] < "7")): # for 2-digit numbers
                    dp[i] += dp[i+2]
        
        return dp[0]


# Solution 1.2: Simple and clear version
class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # dp[n] = 1, dp[n-1] depends on s[n-1]
        prev1 = 1  # dp[i+1]
        prev2 = 1  # dp[i+2]

        # handle last char explicitly to seed prev1 correctly
        # (alternatively, just start loop at i = n-1 as above)
        # We'll use the one-loop style as the first solution did.

        prev1, prev2 = 1, 1
        for i in range(n - 1, -1, -1):
            cur = 0
            if s[i] != '0':
                cur += prev1
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                    cur += prev2
            prev1, prev2 = cur, prev1
        return prev1


# Solution 2: Top Down
class Solution(object):
    def numDecodings(self, s):
        memo = {}

        def decode_helper(index):
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            if index in memo:
                return memo[index]

            ways = decode_helper(index + 1)

            if index + 1 < len(s) and int(s[index: index+2]) <= 26:
                ways += decode_helper(index + 2)

            memo[index] = ways
            return ways

        return decode_helper(0)

# Soluiton 3: Recursion
class Solution(object):
    def numDecodings(self, s):
        def decode_helper(index):
            if index == len(s):
                return 1  # Reached the end, one valid decoding
            if s[index] == '0':
                return 0  # If current digit is '0', it cannot be decoded alone
            ways = decode_helper(index + 1)  # Single-digit decoding
            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                ways += decode_helper(index + 2)  # Two-digit decoding
            return ways
        return decode_helper(0)

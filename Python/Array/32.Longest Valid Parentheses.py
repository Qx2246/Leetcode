# Solution 1:
class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]   # index *before* the current valid block
        max_len = 0

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(output, i - stack[-1])

        return max_len


# Solution 2: pass from both side: left to right & right to left          
class Solution(object):
    def longestValidParentheses(self, s):
        left = right = max_len = 0

        for i in s:
            if i == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                max_len = max(max_len, 2*right)
            elif right > left:
                left = right = 0
        
        left = right = 0
        for ch in reversed(s):
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0

        return max_len


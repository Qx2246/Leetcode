# Solution 1: 
class Solution(object):
    def isValid(self, s):
        # map closing → opening
        stack = []
        parentheses = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in s:
            if i in "([{":                # 1) opener → push
                stack.append(i)
            else:                          # 2) closer
                if not stack or stack.pop() != match[i]:
                    return False           # mismatch or nothing to match with
        return not stack                   # 3) must be empty



# Solution 2: think reversely
class Solution(object):
    def isValid(self, s):
        
        stack = [] #push an opening bracket when we meet one, and pop it off when we see its matching closer.
        parentheses = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in s:
            if i not in parentheses:
                stack.append(i)
            elif not stack or stack[-1] != parentheses[i]:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0


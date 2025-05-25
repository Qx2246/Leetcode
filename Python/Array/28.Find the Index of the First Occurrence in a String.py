# Solution 1
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i
        else: 
            return -1
        
# Solution 2:
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1

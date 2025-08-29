# Solution 1
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0 
        string = ""

        for i in s:
            if i in string:
                string = string[string.index(i) + 1:]

            string += i
            
            max_len = max(max_len, len(string))
        
        return max_len

# Solution 2
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1:
            return 1
        
        st = {}
        left, right = 0, 0
        n = len(s)
        max_len = 0

        while right < n:
            if s[right] in st:
                left = max(left, st[s[right]] + 1)
            length = right - left + 1
            max_len = max(max_len, length)
            st[s[right]] = right
            right += 1
        
        return max_len

# Solution 2.1 (more simple and faster)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        st = {}                 # char -> last seen index
        left = 0                # window left bound
        max_len = 0

        for right, ch in enumerate(s):
            if ch in st and st[ch] >= left:
                # jump left past the previous occurrence
                left = st[ch] + 1
            # window [left, right] has no duplicates now
            max_len = max(max_len, right - left + 1)
            st[ch] = right      # update last seen index

        return max_len

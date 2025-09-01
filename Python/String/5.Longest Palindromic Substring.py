# solution 1: expand from the center
class Solution:
    def longestPalindrome(self, s):
        def expandfromcenter(left, right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1
            return s[left + 1 : right]
        
        longest = ""
        for i in range(len(s)):
            #odd:
            odds = expandfromcenter(i,i)
            #even
            even = expandfromcenter(i, i+1)

            longer = odds if len(odds) > len(even) else even
            if len(longer) > len(longest):
                longest = longer

        return longest



# solution 2: expand from the center using 'helper' 
class Solution:
    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            # odd case, like "aba"
            odds = self.helper(s, i, i)
            if len(odds) > len(longest):
                longest = odds
            # even case, like "abba"
            even = self.helper(s, i, i+1)
            if len(even) > len(longest):
                longest = even
        return longest  


    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]  


# solution 2.1: expand from the center using 'helper' 2.0 concise version
class Solution:
    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            longest = max(self.helper(s,i,i), self.helper(s,i,i+1), longest, key = len)
        return longest


    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]  

class Solution 1:
    def longestPalindrome(self, s):
	def expandfromcenter(left, right):
		while left >= 0 and right < len(s) and s[left] == s[right]:
			left -= 1
			right += 1
		return s[left+1 : right]
	
	longest = ""
	
	for i in range(len(s)):
		odds = expandfromcenter(i,i)
		even = expandfromcenter(i, i+1)
		longer = odds if len(odds) > len(even) else even
		if len(longer) > len(longest):
			longest = longer
	return longest



class solution 2:
	def helper(self, s, left, right):
		while left >= 0 and right < len(s) and s[left] == s[right]:
			left -=1
			right +=1
		return s[left+1 : right]

	def longestPalindrome(self, s):
	longest = ''
	
	for i in range(len(s)):
		odds = self.helper(s,i, i)
		if len(odds) > len(longest):
			longest = odds
		even = self.helper(s, i, i+1)
		if len(even) > len(longest):
			longest = even
	return longest


class solution 2.1:  #concise version compared to solution 2
        def helper(self, s, left, right):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                        left -=1
                        right +=1
                return s[left+1 : right]

        def longestPalindrome(self, s):
		longest = ""
		longest = max(self.helper(s,i,i), self.helper(s,i,i+1), longest, key=len)
	return longest



# Solution 1:
class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        i = 1
        
        while i <= len(strs[0]):
            if strs[0][:i] == strs[-1][:i]:
                i += 1
            else:
                break
    
    return strs[0][:i-1]


# Solution 2: Fatest compared to solution 1 & 3
class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        output = ""
        
        first = strs[0]
        last = strs[-1]        

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            else:
                output += first[i]
        return output



# Solution 3:
class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        i = 1 

        while i <= min(len(strs[0]), len(strs[-1])):
            if strs[0][:i] == strs[-1][:i]:
                i += 1
            else:
                break
        return strs[0][:i-1]



class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        output = ""

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                break
            else:
                output += strs[0][i]
        return output

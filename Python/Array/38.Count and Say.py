class Solution(object):
    def countAndSay(self, n):
        result = "1"
        for i in range(1,n):
            result = self.summarize(result)
        return result

    
    def summarize(self,s):
        result = ""
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                result += str(count) + s[i-1]
                count = 1
        result += str(count) + s[-1] # append the last group

        return result

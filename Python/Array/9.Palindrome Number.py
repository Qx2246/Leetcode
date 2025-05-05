# Solution 1: 
# using reverse, if the reverse == x, then it is true
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        original = x
        reverse = 0

        while x != 0:
            digit = x % 10
            x //= 10
            
            reverse = reverse * 10 + digit

        return reverse == original


# Solution 2: 
# split from the center then compare
class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False
        
        x = str(x)
        length = len(x)

        if length <=1:
            return True

        if length % 2 == 0:
            left = length // 2 - 1
            right = length // 2
        else:
            left = length // 2 - 1
            right = length // 2 + 1

        while left >=0 and right < length:
            if x[left] != x[right]:
                return False
            
            left -=1
            right +=1

        return True


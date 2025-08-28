# Solution 1: Most straight-forward Method
class Solution(object):
    def myPow(self, x, n):

        if n == 0: return 1
        if n == 1: return x

        output = 0
        output += x ** n

        return output

# Solution 2: Recursive
class Solution(object):
    def myPow(self, x, n):
        if not n: 
            return 1  # when n = 0
        if n < 0:
            return 1 / self.myPow(x, -n) 
        if n % 2:
            return x * self.myPow(x, n-1)

        return self.myPow(x*x, n/2)

class Solution(object):
    def multiply(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)

        result = [0] * (n1 + n2) # if n1+n2 = 5, then result = [0,0,0,0,0]

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0')) # '- ord('0')' transfers 'strings' into 'integers'
                total = mul + result[i + j + 1]
                result[i + j + 1] = total % 10
                result[i + j] += total // 10
        
        product = ''.join(map(str, result)).lstrip('0') # convert integers back to strings, and remove all the '0' on the left

        if product:
            return product
        else:
            return "0"


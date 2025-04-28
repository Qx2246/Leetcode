class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse = 0

        while x != 0:
            digit = x % 10
            x //= 10
            
            # 2**31-1 = 2147483647
            if reverse > (2**31-1) // 10 or (reverse == (2**31-1)//10 and digit > 7):
                return 0 
            #-2**31 = −2147483648; 
            if reverse < (-2**31) // 10 or (reverse == (-2**31) // 10 and digit < -8):
                return 0
            
            reverse = reverse * 10 + digit
        
        return reverse * sign # do not forget the sign

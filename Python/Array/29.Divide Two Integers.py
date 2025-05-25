# Solution 1:
class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == divisor:
            return 1
        if divisor == 1:
            return dividend

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31


        if dividend < 0 and divisor > 0:
            output = -(abs(dividend)/divisor)
        elif dividend > 0 and divisor < 0:
            output = -(dividend/abs(divisor))
        elif dividend < 0 and divisor < 0:
            output = (abs(dividend)/abs(divisor))
        else:
            output = (dividend/divisor)
        
        if output > INT_MAX:
            return INT_MAX
        
        if output < INT_MIN:
            return INT_MIN


        return output


# Solution 2:
class Solution(object):
    def divide(self, dividend, divisor):

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        a = abs(dividend)
        b = abs(divisor)
        output = 0

        while a >= b:
            shift = 0
            while a >= (b << shift): # b * 2^shift
                shift += 1
            shift -= 1
            output += 1 << shift
            a -= b << shift

        if (dividend < 0) != (divisor < 0):
            output = -(output)
        
        return output

        '''
        Step-by-step with dividend = 10, divisor = 3:

            a = 10, b = 3

            Loop:

            3 << 0 = 3 → OK

            3 << 1 = 6 → OK

            3 << 2 = 12 → too big → stop

            subtract 6, add 2^1 = 2 to result

            a = 4

            repeat with 3 << 0 = 3 → subtract, add 1 → done

            Final result: 2 + 1 = 3
        '''

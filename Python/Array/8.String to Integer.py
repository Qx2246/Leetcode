# Solution 1:
class Solution(object):
    def myAtoi(self, s):
        num = "0123456789"
        result = ""

        for elem in s:
            if elem == " " and len(result) == 0:
                continue
            if elem != " " and (elem in "-+" or elem in num) and len(result) == 0:
                result += elem
            elif elem in num:
                result += elem
            else:
                break
        
        if result == "" or result in "-+":
            return 0
        else:
            if int(result) < -(2 ** 31):
                return -(2 ** 31)
            elif int(result) > (2 ** 31 - 1):
                return (2 ** 31 - 1)
            else:
                return int(result)


# Solution 2:
class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s or s in "-+":
            return 0
            
        i = 0
        sign = 1
        result = 0

        if s[i] in "-+":
            sign = -1 if s[i] in "-" else 1
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -(2**31)
            result = result * 10 + digit
            i += 1
        
        return sign * result



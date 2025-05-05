# Solution 1:
class Solution:
    def intToRoman(self, num):
        # Creating Dictionary for Lookup
        num_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        # Result Variable
        r = ''

        for key, value in num_map:
            while num >= key:
                r += value
                num -= key
        return r

# Soluion 2:
class Solution:
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = []
        
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                result.append(symbols[i])
        
        return ''.join(result)




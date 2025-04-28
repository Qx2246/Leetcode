# solution 1:
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        result = [''] * numRows
        index = 0
        step = 1

        for x in s:
            result[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(result)


# solution 2:
class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        result = [''] * numRows
        index = 0
        going_up = True

        for x in s:
            result[index] += x
            if index == 0:
                going_up = True
            else index == numRows - 1:
                going_up = False
            
            if going_up is True:
                index += 1
            else:
                 index -= 1

        return ''.join(result)


# solution 3:
class Solution:
    def convert(self, s, numRows):
        pattern = list(range(numRows)) + list(range(numRows - 2, 0, -1)) # pattern n-2, if row = 4, start at 2, stop at 0, and decrease by 1 every single time

        result = [''] * numRows
        for index, value in enumerate(s):
            result[pattern[index % len(pattern)]] += value
        return ''.join(result)








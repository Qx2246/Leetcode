# Solution 1:
class Solution(object):
    def letterCombinations(self, digits):
        letter_map = {
            '2': "abc", 
            '3': "def", 
            '4': "ghi", 
            '5': "jkl",
            '6': "mno", 
            '7': "pqrs", 
            '8': "tuv", 
            '9': "wxyz"
        }

        if not digits or digits == 1:
            return []
        
        output = []

        def backtrack(index, path):
            if index == len(digits):
                output.append("".join(path))
                return
            
            for letter in letter_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return output



# Solution 2:
class Solution(object):
    def letterCombinations(self, digits):
        letter_map = {
            '2': "abc", 
            '3': "def", 
            '4': "ghi", 
            '5': "jkl",
            '6': "mno", 
            '7': "pqrs", 
            '8': "tuv", 
            '9': "wxyz"
        }

        if not digits or digits == 1:
            return []


        output = [""]
        
        # list-comprehension line
        for digit in digits:
            letters = letter_map[digit]
            output = [prefix + letter for prefix in output for letter in letters]
        
        return output

        '''
        # standard way of coding:
        output = [""]
        for digit in digits:
            letters = letter_map[digit]

            result = []
            for prefix in output:
                for letter in letters:
                    result.append(prefix + letter)

            output = result            
        
        return output
        '''

# Solution 1:
class Solution(object):
    def generateParenthesis(self, n):
        def gp(left, right, s):
            if len(s) == n * 2:
                result.append(s)
                return

            if left < n:
                gp(left + 1, right, s + "(" )  # recursive function (a funciton calling itself)
            
            if right < left:
                gp(left, right + 1, s + ")")
            
        result = []
        gp(0,0, '')
        return result



# Solution 2:
class Solution(object):
    def generateParenthesis(self, n):
        def gp(left, right, s):
            if len(s) == n * 2:
                output.append(s)
                return
            
            if left > 0:
                gp(left - 1, right, s + "(")
            
            if right > left:
                gp(left, right - 1, s +")")
            
        
        output = []
        gp(n, n, '')
        return output


# Solution 3: more fancy way
def generateParenthesis(self, n, open=0): # open: how many '(' are currently unmatched (a “stack height”)
    if n > 0 <= open: # == (n > 0) and (open >= 0)
        return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
               [')' + p for p in self.generateParenthesis(n, open-1)]

    return [')' * open] * (not n)

    '''
    There are two situations here:

    a. Valid completion (n == 0):
        not n is True (1), so the list-replication […] * 1 keeps the element.
        We append open closing brackets to seal the string (e.g. if open==2, add " ))").

    b. Invalid path or no more opens and too many closes (open < 0 or both
    conditions in the if failed while n > 0):
        not n is False (0), so […] * 0 produces an empty list, effectively
        pruning that branch from the search tree.
    '''

# Solution 1: DFS
class Solution(object):
    def permute(self, nums):
        res = []

        def dfs(nums, path):
            if not nums:
                res.append(path)
                return

            for i in range(len(nums)): 
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])

        dfs(nums, [])
        return res
        

# Solution 2: Back-tracking Method
class Solution:
    def permute(self, nums):
        res = []
        visited = [False] * len(nums)
        # a boolean list keeping track of whether each number in nums has already been used in the current permutation.
        # visited = [False, False, False]

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
                # If the length of path is the same as nums, that means we’ve chosen all numbers → we found a valid permutation.

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True # Mark the number as used and add it to the current path.
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
                    visited[i] = False # Undo everything allowing the algorithm to try other possibilities.

        dfs([])
        return res


# Solution 1: Depth-First Search (DFS) with backtracking
class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        self.dfs(candidates, target, [], result)
        return result

    def dfs(self, nums, target, path, result):
        if target < 0:
            return # return back to the last stack
        if target == 0:
            result.append(path)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[i:], target - nums[i], path + [nums[i]], result)

# Solution 1: In-place backtracking with used[]
class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()                 # sort so duplicates are adjacent
        res = []
        used = [False] * len(nums)  # track which indices are in the current path

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicates: if current equals previous and previous wasn't used,
                # then picking nums[i] here would create a duplicate branch.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return res


# Solution 2: Slicing version with per-level de-dup (simple & clean)
class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        res = []

        def dfs(remaining, path):
            if not remaining:
                res.append(path)
                return
            
            prev = None
            for k, v in enumerate(remaining):
                if v == prev:
                    continue
                dfs(remaining[:k] + remaining[k+1 : ], path + [v])
                prev = v
            
        dfs(nums, [])
        return res

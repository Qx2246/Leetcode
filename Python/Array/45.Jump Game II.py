# Solution using BFS (Breadth-First Search)
    # a common algorithm used to explore or search a graph or tree level by level
    # finding shortest paths or level-by-level exploration
class Solution(object):
    def jump(self, nums):
        ans = 0
        end = 0
        farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            
            if farthest >= (len(nums) - 1):
                ans += 1
                break
            
            if i == end:  # Visited all the items on the current level
                ans += 1  # Increment the level
                end = farthest  # Make the queue size for the next level

        return ans

# Solution 1:
class Solution(object):
    def trap(self, height):

        n = len(height)
        
        if n == 0:
            return 0

        left = [0] * n
        right = [0] * n

        # fill the left array
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])

        # fill the right arry
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        water_unit = 0
        for i in range(n):
            water_unit += min(left[i], right[i]) - height[i]

        return water_unit       

# Solution 2:
class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        left_max, right_max = -1, -1
        water_unit = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                water_unit += left_max - height[left]
                left += 1
            else:
                water_unit += right_max - height[right]
                right -= 1
        
        return water_unit

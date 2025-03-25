class Solution(object):
    def maxArea(self, height):
        max_water = 0
        water_height = 0
        water_width = len(height) - 1

        while water_height != water_width:
            n = min(height[water_height],height[water_width])
            water = n * (water_width - water_height)
            if water > max_water:
                max_water = water
            if n == height[water_height]:
                water_height += 1
            else:
                water_width -= 1
        
        return max_water

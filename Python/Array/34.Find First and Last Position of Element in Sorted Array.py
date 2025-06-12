# Solution 1:
class Solution(object):
    def searchRange(self, nums, target):
        
        def search(x):
            low = 0
            high = len(nums)

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            return low

        low = search(target)
        high = search(target+1)-1

        if low <= high:
            return [low, high]

        return [-1, -1]


# Solution 2:
class Solution(object):
    def first_pos(self, nums, target, n):
        result = -1
        start, end = 0, n

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                result = mid
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1 # keep searching to narrow down the range and find the first pos
            else:
                end = mid - 1
        return result

    
    def last_pos(self, nums, target, n):
        result = -1
        start, end = 0, n

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                result = mid
                start = mid + 1 # keep searching to narrow down the range and find the last pos
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return result
        
    def searchRange(self, nums, target):
        n = len(nums) - 1

        fp = self.first_pos(nums, target, n)
        lp = self.last_pos(nums, target, n)

        return [fp, lp]


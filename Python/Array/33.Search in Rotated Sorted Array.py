# Solution 1:
class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return -1

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                i += 1

# Solution 2: Binary Search
class Solution(object):
    def search(self, nums, target):

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) / 2
            if target == nums[mid]:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target and nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid -1

        return -1

# Solution 1: use set()
class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)
'''
common wrong:
	nums = sorted(set(nums))
	return len(nums)

# nums =  doesn't replace elements in the original list.
# nums[:] = replaces element in place
'''


# Solution 2: Two-pointers
class Solution(object):
    def removeDuplicates(self, nums):
        slow, fast = 0, 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                slow += 1
                fast += 1
        
        return slow + 1 # There are slow + 1 unique elements total, since indices start at 0.


# Solution 2.1 (faster & more organized version of solution 2)
class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0

        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


# Solution 3: using .pop()
class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        
        return len(nums)


# Solution 4: using OrderedDict.fromkeys()
from collections import OrderedDict

class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = OrderedDict.fromkeys(nums)
        return len(nums)

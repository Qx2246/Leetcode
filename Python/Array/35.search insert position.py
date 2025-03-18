# Look for the target from two sides
class Solution(object):
     def searchInsert1(self, nums, target):
        high = len(nums) - 1
        low = 0
        while low <= high:
            mid = low + (high - low) // 2 # Get the median
            if nums[mid] == target: # return the index if equals to the target
                return mid
            elif nums[mid] < target: # index + 1 if smaller than the target
                low = mid + 1
            else:
                high = mid - 1 # index - 1 if larger than the target
        return low



def searchInsert2(self, nums, target):
    high = len(nums) - 1
    low = 0
    while low <= high:
        mid = low + (high - low) // 2
        if num[mid] == target:
            return mid
        elif num[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return high


# Faster in dealing with small unsorted List
class Solution(object):
    def searchInsert3(self, nums, target):
        for i in range(len(nums)):  # Loop through the list
            if nums[i] >= target:   # If the current number is greater or equal to target
                return i            # Return the index
        return len(nums)            # If target is larger than all elements, return the length


# Faster in dealing with small sorted List
# Start from the left side seeking for the target
class Solution(object):
    def searchInsert4(self, nums, target):
        return bisect.bisect_left(nums, target)def searchInsert1(self,nums,target):
	high = len(nums) -1
	low = 0
	while low <= high:
		mid = low + (high - low) // 2
		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			high = mid - 1
		else:
			low = mid + 1
	return high


def searchInsert2(self, nums, target):
	for i in range(len(nums)):
		if nums[i] >= target:
			return i
	return len(nums)

def searchInsert3(self, nums, target):
	return bisect.bisect_left(nums,target)


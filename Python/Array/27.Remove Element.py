# Solution 1: using .pop()
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0

        for i in range(len(nums)):
            if nums[i] == val:
                nums.pop(i)
	    else:
                count += 1
        
        return count


# Solution 1.1: advance and more safe .pop() version
class Solution(object):
    def removeElement(self, nums, val):
        count = i = 0

        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return count

# Solution 2: using .append(), but not the best way as it did not change nums in-place
class Solution(object):
    def removeElement(self, nums, val):
        output = []

        for i in range(len(nums)):
            if nums[i] != val:
                output.append(nums[i])
        
        # Now copy the valid elements back into nums
        for i in range(len(output)):
            nums[i] = output[i]

        return len(output)


# Solution 3: Two-pointers (more advanced solution)
class Solution(object):
    def removeElement(self, nums, val):
        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        
        return j


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        output = []
        n = len(nums)

        for i in range(n - 2):                       # need at least 3 numbers
            if i > 0 and nums[i] == nums[i - 1]:     # skip duplicate anchors
                continue

            left, right = i + 1, n - 1               # pointers *after* i
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicates on both sides
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:                           # need a larger sum
                    left += 1
                else:                                # need a smaller sum
                    right -= 1

        return output


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')  # 'inf' makes sure the result is infinitive
        #closest = 100 or just assume a random number (large enough)

        output = 0

        for i in range(len(nums)-2):

            left = i + 1
            right = len(nums) - 1

            if len(nums) == 3:
                output = nums[i] + nums[left] + nums[right]

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total - target)

                if diff < closest:
                    closest = diff
                    output = total

                if total == target:
                    output = total
                else:
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                
        return output
                    

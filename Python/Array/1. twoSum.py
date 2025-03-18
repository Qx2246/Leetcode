Solution 1:

    # nums[i] + nums[j] = target
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



Solutioin 2:

    # nums[j] = target - nums[i]
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            sub = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == sub:
                    return [i, j]


Solution 3:

    # use dictionary (index, value)
    def twoSum(self, nums, target):
        d = {}

        for index, value in enumerate(nums):
            sub = target - value

            if sub in d:
                return [d[sub],index]
            
            d[value] = index

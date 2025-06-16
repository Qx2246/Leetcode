# Solution 1:
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        n = len(candidates)

        def dfs(start, target, path):
            if target < 0:
                return
            if target == 0:
                result.append(list(path))
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i+1, target - candidates[i], path + [candidates[i]]) # keep [candidates] in an individual [].
    
        dfs(0,target, [])
        return result
        
# Solution 2:
class Solution:
    def combinationSum2(self, candidates, target):
        
        #setup
        result = []
        combination = []
        candidates.sort() #to group the same candidates together

        def dfs(index,target):

            #is a solution
            if target == 0: 
                result.append(list(combination))
                return

            elif index < len(candidates): #do unconsiderd candidates remain?
                if target >= candidates[index]: #is it possible to add more candidates to combination and get a solution?

                    combination.append(candidates[index])
                    dfs(index+1, target - candidates[index]) #with candidate at this index and all equivalents before index
                    combination.pop()

                    # without candidate at this index and any equivalents after index
                    for i in range(index+1,len(candidates)): #
                        if candidates[index] != candidates[i]:
                            dfs(i,target) #with next unique candidate
                            break

        dfs(0,target) # construction of result
        return result # return after construction

class Solution(object):
    def twoSumBruteForce(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    def twoSumComplement(self, nums, target):
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i
        return []
    

solver = Solution()
print(solver.twoSumComplement([3, 2, 4], 6))
        
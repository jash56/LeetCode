class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and i != hashmap[complement]:
                return [i, hashmap[complement]]
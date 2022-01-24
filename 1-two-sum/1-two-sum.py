class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = {}
        
        for i in range(len(nums)):
            complement[nums[i]] = i
        print(complement)
        
        for i in range(len(nums)):
            if target - nums[i] in complement and i != complement[target - nums[i]]:
                return [i, complement[target - nums[i]]]
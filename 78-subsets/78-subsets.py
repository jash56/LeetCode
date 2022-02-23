class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:    
        
        def rec(nums):
            nonlocal ans
            if not nums:
                ans.add(nums)
                return
            
            ans.add(nums)
            
            for i in range(len(nums)):
                rec(tuple(nums[:i]+nums[i+1:]))
        
        ans = set()
        rec(tuple(nums))

        return ans
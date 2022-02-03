class Solution:
                
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2: return max(nums)
        
        dp = [None] * (len(nums)+1)
        dp[-1], dp[-2] = 0, nums[-1]
        for i in range(len(nums)-2, -1, -1):
            # print(dp, i)
            dp[i] =  max(dp[i+2] + nums[i], dp[i+1])
            
        
        return dp[0]
    
    
    
#memoization
#     def rob_skip(self, nums, curr, memo):
#         if curr >= len(nums):
#             return 0
        
#         if memo[curr]:
#             return memo[curr]
        
#         memo[curr] = max(nums[curr] + self.rob_skip(nums, curr+2, memo), self.rob_skip(nums, curr+1, memo))
        
#         return memo[curr]
        
        
#     def rob(self, nums: List[int]) -> int:
#         memo = [0] * len(nums)
#         ans = self.rob_skip(nums, 0, memo)
#         return ans
    
# recursive
#     def rob_skip(self, nums, curr):
#         if curr >= len(nums):
#             return 0        
#         return max(nums[curr] + self.rob_skip(nums, curr+2), self.rob_skip(nums, curr+1))
               
#     def rob(self, nums: List[int]) -> int:
#         ans = self.rob_skip(nums, 0)
#         return ans
    
    
    
            
        
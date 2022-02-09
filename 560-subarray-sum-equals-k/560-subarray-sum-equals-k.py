class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = curr_sum = 0
        prefix = defaultdict(int)               

        for num in nums:
            curr_sum += num
            if curr_sum == k:
                ans += 1                           
            ans += prefix[curr_sum-k]                
            prefix[curr_sum] += 1            
        return ans
    
    
#         ans = 0
#         prefix = [0] * (len(nums)+1)
        
#         for i in range(1,len(nums)+1):
#             prefix[i] = nums[i-1] + prefix[i-1]
    
#         for start in range(len(prefix)):
#             for end in range(start+1, len(prefix)):
#                 if prefix[end] - prefix[start] == k:
#                     ans += 1     
#         return ans
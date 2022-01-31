class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0
        nums = sorted(list(set(nums)))
        print(nums)
        max_len = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i] - 1:
                max_len = max(curr, max_len)
                curr = 0
            curr += 1   
        
        return max(curr, max_len)
            
        
        
        
        
        
        
        
        
        
        
        


        
        
        
        
        
#         if not nums: return 0
#         nums = list(set(nums))
#         nums.sort()
#         longest_len = curr_len = 1
#         i = 0

#         while i < len(nums)-1:
#             if nums[i] + 1 != nums[i+1]:
#                 longest_len = max(longest_len, curr_len)
#                 curr_len = 0

#             i += 1
#             curr_len += 1 

#         return max(longest_len, curr_len)
        
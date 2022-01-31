class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0
        nums = sorted(list(set(nums)))
        max_len = curr_len = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i] - 1:
                max_len = max(curr_len, max_len)
                curr_len = 0
            curr_len += 1          
        return max(curr_len, max_len)
        
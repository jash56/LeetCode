class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float('-inf')
        curr_sum = 0
        for i in nums:
            curr_sum = max(i, curr_sum+i)
            print(curr_sum, i)
            max_sum = max(max_sum, curr_sum)
        return max_sum
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0
        nums = list(set(nums))
        nums.sort()
        longest_len = curr_len = 1
        i = 0
        print(nums)
        while i < len(nums)-1:
            if nums[i] + 1 != nums[i+1]:
                longest_len = max(longest_len, curr_len)
                curr_len = 0
                # i -= 1
                print(longest_len)

            i += 1
            curr_len += 1 

        return max(longest_len, curr_len)
        
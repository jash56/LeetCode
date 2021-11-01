import numpy as np
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        nums = np.array(nums)
        count = 0
        while True:
            maximum_index = np.argmax(nums)
            maximum = nums[maximum_index]
            minimum = np.min(nums)
            if maximum == minimum:
                break
            else:
                nums += (maximum - minimum)
                nums[maximum_index] -= (maximum - minimum)
                count += (maximum - minimum)

        return count
        
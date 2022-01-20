class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums) - 1
        
        if nums[0] > nums[-1]:
            if target == nums[0]:
                return 0
            elif target < nums[0]:
                start = nums.index(min(nums))
            else:
                end = nums.index(min(nums))
            print(start, end)
          
        while end >= start:
            mid = (end+start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1   
        return -1
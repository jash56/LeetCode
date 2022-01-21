class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        if nums[0] < nums[-1]: return nums[0]
        
        start, end = 0, len(nums)-1
        while start <= end:
            
            mid = (start+end) // 2
            
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[end] < nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
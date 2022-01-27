class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        def get_min(nums):
            
            start, end = 0, len(nums)-1
            
            while start < end:
                mid = (start+end)//2
                if nums[mid] > nums[mid+1]:
                    return mid+1
                elif nums[mid-1] > nums[mid]:
                    return mid
                elif nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1    
                
        start, end = 0, len(nums) - 1
        if nums[0] > nums[-1]:

            if target < nums[0]:
                start = get_min(nums)
            else:
                end = get_min(nums)
                
        while end >= start:
            mid = (end+start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1   
        return -1
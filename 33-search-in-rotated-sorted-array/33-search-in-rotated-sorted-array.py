class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def get_min(num_list):
            left = 0
            right = len(num_list) - 1
            while left <= right:
                mid = (left+right)//2
                if num_list[mid] > num_list[mid + 1]:
                    return mid + 1
                elif num_list[mid] < num_list[left]:
                    right = mid
                else:
                    left = mid         
                
        start, end = 0, len(nums) - 1
        if nums[0] > nums[-1]:
            if target == nums[0]:
                return 0
            elif target < nums[0]:
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
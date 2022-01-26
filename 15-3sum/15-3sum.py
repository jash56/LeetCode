class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            start, end = i+1, len(nums)-1
            while start < end:
                temp = nums[start] + nums[end] + nums[i]
                if temp == 0:
                    ans.add((nums[i], nums[start], nums[end]))
                    if nums[start] == nums[start+1]:
                        start += 1
                    elif nums[end] == nums[end-1]:
                        end -= 1
                    else:
                        start += 1
                        end -= 1
                elif temp > 0:
                    end -= 1
                else:
                    start += 1
            
        return [list(x) for x in ans]
                    
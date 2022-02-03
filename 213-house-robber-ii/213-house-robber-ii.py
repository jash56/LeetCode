class Solution:
    def get_loot(self, house_list):
        
        next_house = house_list[-1]
        next_next_house = 0        
        for i in range(len(house_list)-2, -1, -1):           
            curr = max(house_list[i]+next_next_house, next_house)         
            next_house, next_next_house = curr, next_house       
        return curr
        
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)
        return max(self.get_loot(nums[:-1]), self.get_loot(nums[1:]))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}
        
        for index, ele in enumerate(nums):
            hash_map[ele] = index

        for index, i in enumerate(nums):
            comp = target - i
            if comp in hash_map and index != hash_map[comp]:
                return [hash_map[comp], index]
            
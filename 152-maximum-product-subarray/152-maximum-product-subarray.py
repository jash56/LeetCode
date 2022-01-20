class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
#         max_product = float('-inf')
#         product = 1
#         for i in range(len(nums)):
#             product *= nums[i]
#             max_product = max(max_product, product)
#             if product == 0: product = 1
                
#         product = 1
#         for i in range(len(nums)-1, -1, -1):
#             product *= nums[i]
#             max_product = max(max_product, product)
#             if product == 0: product = 1


        max_so_far = min_so_far = max_product = nums[0]
    
        for i in nums[1:]:
            max_so_far, min_so_far = max(i, max_so_far*i, min_so_far*i), min(i, max_so_far*i, min_so_far*i)
            
            max_product = max(max_product, max_so_far)
        return max_product
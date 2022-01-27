class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         pre = [1] * (len(nums))
#         post = [1] * (len(nums))
#         for i in range(1, len(nums)):
#             pre[i] = pre[i-1] * nums[i-1]        
#         for i in range(len(nums)-2, -1, -1):
#             post[i] = post[i+1] * nums[i+1]
        
#         return [pre[i] * post[i] for i in range(len(nums))]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        n = len(nums)
        prefix, postfix = [1] * n, [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            postfix[n-i-1] = postfix[n-i] * nums[n-i]
    
        return [prefix[i] * postfix[i] for i in range(len(nums))]
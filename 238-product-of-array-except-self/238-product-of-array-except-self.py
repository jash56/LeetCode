class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1] * (len(nums))
        post = [1] * (len(nums))
        for i in range(1, len(nums)):
            print(i)
            pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
        
        return [pre[i] * post[i] for i in range(len(nums))]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        n = len(nums)
        prefix, postfix, answer = [1] * n, [1] * n, [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            postfix[n-i-1] = postfix[n-i] * nums[n-i]
        for i in range(n):
            answer[i] = prefix[i] * postfix[i]
        return answer
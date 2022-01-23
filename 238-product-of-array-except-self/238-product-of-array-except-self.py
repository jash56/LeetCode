class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, postfix = [1] * n, [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            postfix[n-i-1] = postfix[n-i] * nums[n-i]
        
        answer = [i*j for i, j in zip(prefix, postfix)]
        return answer
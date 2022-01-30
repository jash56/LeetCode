class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = k+1  
        left = right = 0
        frequency = {}
        
        while right < len(s):

            frequency[s[right]] = frequency.get(s[right], 0) + 1
            
            if (right-left+1) - max(frequency.values()) <= k:
                ans = max(ans, right-left+1)
            else:
                
                frequency[s[left]] -= 1
                left += 1
            right += 1
            
            print(left, right, ans)
            
        return ans
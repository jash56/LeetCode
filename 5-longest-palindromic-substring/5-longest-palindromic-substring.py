class Solution:
    def longestPalindrome(self, s: str) -> str: 
        ans = s[0]
        for i in range(1, len(s)):            
            left, right = self.longest_substring(s, i-1, i)
            temp1 = s[min(len(s)-1, left+1):max(0, right-1)+1]
            left, right = self.longest_substring(s, i, i)
            temp2 = s[min(len(s)-1, left+1):max(0, right-1)+1]
            # print(temp2, 'temp2')
            if len(temp1) > len(temp2):
                temp = temp1
            else:
                temp = temp2          
            if len(ans) < len(temp):
                ans = temp
        return ans
                
    def longest_substring(self, s, left, right):     
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return left, right 
            left -= 1
            right += 1           
        return left, right
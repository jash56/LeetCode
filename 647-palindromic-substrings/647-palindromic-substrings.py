class Solution:
    
    def countSubstrings(self, s: str) -> int:        
        ans = 1
        for i in range(1, len(s)):          
            ans += self.palindrome_from_center(s, i, i)
            ans += self.palindrome_from_center(s, i-1, i)
        return ans
    
    def palindrome_from_center(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s):
            
            if s[left] == s[right]:
                count += 1
            else:
                break
            left -= 1
            right += 1
        return count
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def is_palindrome(self, s):
        
#         start, end = 0, len(s)-1
#         while start < end:
#             if s[start] != s[end]:
#                 return False
#         return True
    
#     def countSubstrings(self, s: str) -> int:
#         ans = 0
#         valid = set()
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if self.is_palindrome(valid, s[i:j+1]):
#                     ans += 1
#         return ans
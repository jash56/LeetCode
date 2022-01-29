class Solution:
    
    def is_palindrome(self, s):
        
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def countSubstrings(self, s: str) -> int:
        ans = 0
        valid = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] not in valid:
                    if self.is_palindrome(s[i:j+1]):
                        ans += 1
                        valid.add(s[i:j+1])
                else:
                    ans += 1
        return ans
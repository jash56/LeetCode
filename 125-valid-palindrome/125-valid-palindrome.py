class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        input_list = []
        for i in s:
            if i.isalnum():
                input_list.append(i.lower())
            
        s = ''.join(input_list)
        
        start, end = 0, len(s) - 1
        while start < end:
            
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        return True
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        input_list = []
        for i in s:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                input_list.append(i)
            elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                input_list.append(i.lower())
            elif ord('0') <= ord(i) <= ord('9'):
                input_list.append(i)
        s = ''.join(input_list)
        
        start, end = 0, len(s) - 1
        while start < end:
            
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        return True
        
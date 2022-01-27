class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0 or len(s) == 1: return len(s)
        
        start = 0
        longest_len = 1

        for end in range(1, len(s)):
            print(start, end, longest_len)
            if s[end] in s[start:end]:
                longest_len = max(end - start, longest_len)
                start = s.index(s[end], start, end) + 1
                
        return max(end - start + 1, longest_len)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         max_len = start = 0
#         char_index = {}
        
#         for end in range(len(s)):            
#             if s[end] in char_index:
#                 start = max(start, char_index[s[end]] + 1)

#             char_index[s[end]] = end
#             max_len = max(end - start + 1, max_len)
                          
#         return max_len  
     
        
#         max_len = start = end = 0
#         while end < len(s):
#             if s[end] not in s[start:end]:
#                 max_len = max(max_len, end - start + 1)
#                 print(max_len, s[start:end+1])
#                 end += 1
#             else:
#                 start = s.index(s[end], start) + 1
#         return max_len
                
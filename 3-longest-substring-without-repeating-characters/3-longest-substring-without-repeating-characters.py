class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = curr_len = start = 0
        # char_index = {}
        for end in range(len(s)):
            if s[end] not in s[start:end]:
                curr_len += 1
                # print(s[end])
            else:
                print(start, s[start:end+1], end)
                max_len = max(curr_len, max_len)
                start = s.index(s[end], start, end) + 1
                curr_len = len(s[start:end+1])
        max_len = max(curr_len, max_len)
                          
        return max_len
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # max_length = curr_length = 0
        # ptr = 0
        # for i in range(len(s)):
        #     if s[i] not in s[ptr:i]:
        #         curr_length += 1
        #         print(curr_length)
        #     else:
        #         max_length = max(max_length, curr_length)
        #         ptr = s.index(s[i], ptr)
        #         curr_length = len(s[ptr:i+1])
        # max_length = max(max_length, curr_length)
        # return max_length
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         max_len = start = end = 0
#         while end < len(s):
#             if s[end] not in s[start:end]:
#                 max_len = max(max_len, end - start + 1)
#                 print(max_len, s[start:end+1])
#                 end += 1
#             else:
#                 start = s.index(s[end], start) + 1
#         return max_len
                
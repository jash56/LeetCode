class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = start = end = 0
        while end < len(s):
            if s[end] not in s[start:end]:
                max_len = max(max_len, end - start + 1)
                print(max_len, s[start:end+1])
                end += 1
            else:
                start = s.index(s[end], start)+1
        return max_len
                
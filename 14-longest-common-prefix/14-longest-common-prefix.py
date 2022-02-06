class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        while len(strs) > 1:
            str1 = strs.pop()
            str2 = strs.pop()
            j = 0
            while j < min(len(str1), len(str2)):
                if str1[j] != str2[j]:
                    break
                j += 1
            strs.append(str1[:j])         
        
        return strs[0]
from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_match = collections.defaultdict(list)       
        ans = []
        for string in strs:
            string_freq = [0] * 26
            for char in string:
                string_freq[ord(char)-ord('a')] += 1 
            anagram_match[tuple(string_freq)].append(string)
        
        for group in anagram_match.values():
            ans.append(list(group))
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         hashmap = defaultdict(list)
#         for word in strs:
#             temp = [0] * 26
#             count_dict = Counter(word)
#             for key, val in count_dict.items():
#                 temp[ord(key)-ord('a')] = val
            
#             hashmap[tuple(temp)].append(word)
#         return hashmap.values()
            
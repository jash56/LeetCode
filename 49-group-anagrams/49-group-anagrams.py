from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_match = collections.defaultdict(list)       

        for string in strs:
            string_freq = [0] * 26
            for char in string:
                string_freq[ord(char)-ord('a')] += 1 
            anagram_match[tuple(string_freq)].append(string)

        return anagram_match.values()
            
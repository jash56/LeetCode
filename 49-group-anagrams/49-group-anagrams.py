from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        hashmap = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            count_dict = Counter(word)
            for key, val in count_dict.items():
                temp[ord(key)-ord('a')] = val
            
            hashmap[tuple(temp)].append(word)
        return hashmap.values()
            
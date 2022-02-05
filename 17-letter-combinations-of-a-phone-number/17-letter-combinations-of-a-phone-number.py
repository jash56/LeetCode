class Solution:
    
    def rec(self, digits, mapping, curr_path, ans):
        if len(digits) == 1:
            for i in mapping[int(digits[0])]:
                ans.append(curr_path + i)
            return
                
        for i in mapping[int(digits[0])]:  
            self.rec(digits[1:], mapping, curr_path + i, ans)
        
                
        
        
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return
        ans = []
        curr_path = ''
        mapping = {
            2: {'a', 'b', 'c'},
            3: {'d', 'e', 'f'},
            4: {'g', 'h', 'i'},
            5: {'j', 'k', 'l'},
            6: {'m', 'n', 'o'},
            7: {'p', 'q', 'r', 's'},
            8: {'t', 'u', 'v'},
            9: {'w', 'x', 'y', 'z'},
        }
        self.rec(digits, mapping, curr_path, ans)
        return ans
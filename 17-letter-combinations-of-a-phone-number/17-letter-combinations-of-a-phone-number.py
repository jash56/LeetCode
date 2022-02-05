class Solution:
    
    def rec(self, digits, mapping, curr_path, ans):
        if not digits:
            ans.append(''.join(curr_path))
            return
                
        for i in mapping[int(digits[0])]: 
            curr_path.append(i)
            self.rec(digits[1:], mapping, curr_path, ans)   
            curr_path.pop()  
            
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return
        ans = []
        curr_path = []
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
class Solution:
    
    def is_valid(self, bracket_list):
        stack = []
        for bracket in bracket_list:
            
            if bracket == '(':
                stack.append(bracket)
            else:
                if not stack:
                    return False
                stack.pop()
        if not stack:
            return True
        else:
            return False
        
    def generateParenthesis(self, n: int) -> List[str]:
        
        open_count = close_count = n
        ans = []
        brackets = []
        
        def rec(brackets, open_count, close_count):
            nonlocal ans
            if open_count == 0 and close_count == 0:   
                if self.is_valid(brackets):
                    ans.append(''.join(brackets))
                return
            if open_count > 0:
                rec(brackets + ['('], open_count - 1, close_count)
            if close_count > 0:
                rec(brackets + [')'], open_count, close_count - 1)
        rec(brackets, open_count, close_count)
        return ans
            
            
            
            
            
            
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = ['#']
        
        for i in s:
            if i =='(' or i =='[' or i =='{':
                stack.append(i)
            elif (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):
                stack.pop(-1)
            else:
                return False
        
        if stack[-1] == '#': return True
        else: return False
                
            
            
            
                
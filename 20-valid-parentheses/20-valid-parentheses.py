class Solution(object):
    def isValid(self, s):

        valid_bracket = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for i in s:  
            if i in valid_bracket:
                if not stack or stack.pop(-1) != valid_bracket[i]:
                    return False
            else:    
                stack.append(i)
        print(stack)
        return not stack
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                if stack:
                    top_element = stack.pop()
                else: return False
                if mapping[char] != top_element:
                    return False
            else:  
                stack.append(char)

        return not stack
class Solution(object):
    def isValid(self, s):

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
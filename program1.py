class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping:
                top_elem = stack.pop() if stack else '#'
                if mapping[char] != top_elem:
                    return False
            else:
                stack.append(char)
        
        return not stack
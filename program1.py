class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping:
                # If the current character is a closing bracket
                top_element = stack.pop() if stack else '#'
                if mapping[char] == top_element:
                    return False
            else:
                # If the current character is an opening bracket
                stack.append(char)
        
        # If the stack is empty at the end, all parentheses are correctly matched
        return not stack
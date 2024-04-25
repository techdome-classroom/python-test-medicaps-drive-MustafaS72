class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Initialize the total value and previous value
        total = 0
        prev_value = 0
        
        # Iterate through the string from right to left
        for char in reversed(s):
            value = roman_values[char]
            
            # If current value is less than previous value, it's a subtraction case
            if value < prev_value:
                total -= value
            else:
                total += value
            
            # Update the previous value for the next iteration
            prev_value = value
        
        return total
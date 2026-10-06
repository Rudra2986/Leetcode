class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_count = 0
        right_count = 0
        
        for char in s:
            if char == '(':
                left_count += 1
            else:
                if left_count > 0:
                    left_count -= 1
                else:
                    right_count += 1
                    
        return left_count + right_count

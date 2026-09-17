class Solution:
    def maxDepth(self, s: str) -> int:
        p_count = 0
        op = 0
        for i in s:
            if i == '(':
                p_count += 1
            if op < p_count :
                op += 1
            if i == ')':
                p_count -= 1
        return op
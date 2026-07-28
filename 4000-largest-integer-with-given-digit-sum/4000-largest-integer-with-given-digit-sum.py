class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        
        op = []
        final = 0
        
        if s > 9 * n:
            return -1
            
        while s != 0:
            if s > 9:
                op.append(9)
                s -= 9
            else:
                op.append(s)
                s = 0

        while len(op) < n :
            op.append(0)
            
        for i in op:
            final = (final*10) + i
            
            
        
        return final
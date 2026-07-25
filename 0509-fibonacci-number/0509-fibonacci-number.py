class Solution:
    def fib(self, n: int) -> int:
        prev1 = 1
        prev2 = 0
        next = 0

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        for i in range(1,n):
                next = prev1 + prev2
                a = prev1
                prev1 = next
                prev2 = a
        return next
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddsum = 0
        evensum = 0

        for i in range(n):
            oddsum += (2*i+1)
            evensum += (2*i + 2)

        while evensum != 0:
            a = evensum
            evensum = oddsum % evensum
            oddsum = a
        
        return oddsum
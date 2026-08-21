class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        op = 0

        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in freq:

            while freq[i] > 1:
                op += 2
                freq[i] -= 2
        
        for i in freq:
            if freq[i] == 1:
                op += 1
                break
        
        return op
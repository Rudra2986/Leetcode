class Solution:
    def strStr(self, h: str, n: str) -> int:
        
        i = 0

        while i <= len(h)-len(n):

            j = 0
            while j < len(n):
                if h[i+j] != n[j]:
                    break
                j += 1

            if j == len(n):
                return i

            i += 1

        return -1
class Solution:
    def smallestPalindrome(self, s: str) -> str:

        s = "".join(sorted(s))
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        op = [0]*len(s)

        left = 0
        right = len(s) - 1

        for i in freq:
                while freq[i] != 0:
                    if freq[i] >= 2:
                        op[left] = op[right] = i
                        freq[i] -= 2
                        left += 1
                        right -= 1
                    else:
                        op[len(s)//2] = i
                        freq[i] -= 1

        return "".join(op)
            
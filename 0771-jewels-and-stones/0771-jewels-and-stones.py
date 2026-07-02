class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        op = 0
        for i in stones:
            if i in jewels:
                op += 1
        return op
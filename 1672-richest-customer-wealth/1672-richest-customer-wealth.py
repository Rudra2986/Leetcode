class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        total = 0
        for i in accounts:
            x = 0
            for j in i:
                x += j
            if x > total:
                total = x
        return total
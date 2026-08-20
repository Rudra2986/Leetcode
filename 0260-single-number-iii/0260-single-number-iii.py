class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for i in nums:
            xor ^= i

        bit = xor & -xor

        a = 0
        b = 0

        for i in nums:
            if i & bit:
                a ^= i
            else:
                b ^= i

        return [a, b]
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        freq = []

        for i in nums:
            if i == 1:
                max_count += 1
            else:
                freq.append(max_count)
                max_count = 0
        freq.append(max_count)
        return max(freq)
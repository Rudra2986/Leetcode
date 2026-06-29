class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        output = []
        total = 0
        for i in nums:
            total += i
            output.append(total)
        return output

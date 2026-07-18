class Solution:
    def findGCD(self, nums: list[int]) -> int:
        nums.sort()
        min = nums[0]
        max = nums[-1]

        # GCD(max, min)
        while min != 0:
            a = min
            min = max % min
            max = a
        
        return max

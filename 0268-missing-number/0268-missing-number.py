class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total1 = 0
        total2 = 0

        for i in range(len(nums)):
            total1 +=nums[i] 
            total2 += i+1

        return (total2 - total1)
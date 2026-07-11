class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        pt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pt], nums[i] = nums[i], nums[pt]
                pt += 1
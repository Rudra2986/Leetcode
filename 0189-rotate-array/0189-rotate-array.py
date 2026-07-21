class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        if k > len(nums):
            k = k % len(nums)

        slicer = len(nums) - k
        nums[:] = nums[slicer:] + nums[:slicer]
        
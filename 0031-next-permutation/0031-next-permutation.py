class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        pivot = -1

        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i - 1
                break

        if pivot == -1:
            nums.reverse()
            return
        
        for i in range(n-1, pivot, -1):
            if nums[pivot] < nums[i]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                nums[pivot + 1:] = nums[pivot + 1:][::-1]
                break

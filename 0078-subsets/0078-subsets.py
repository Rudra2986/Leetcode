class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        mask = 0
        ans = []
        while (mask < (1 << len(nums))):
            subset = []
            for i in range(len(nums)):
                if ( mask & (1 << i) ):
                    subset.append(nums[i])
            ans.append(subset)
            mask += 1
        return ans
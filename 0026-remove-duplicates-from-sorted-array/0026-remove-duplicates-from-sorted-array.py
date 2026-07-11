class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new = []
        for i in nums:
            if i not in new:
                new.append(i)
        for i in range(len(new)):
            nums[i] = new[i]
        return len(new)
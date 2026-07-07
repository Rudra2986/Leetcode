class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        ans = 0
        for i in freq:

            if (freq[i] > (len(nums)/2)) and (freq[i] >= ans):
                ans = i
        return ans
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = []
        negative = []
        op = []
        n= len(nums)

        for i in nums:
            if i >= 0 :
                positive.append(i)
            else:
                negative.append(i)

        for i in range(n//2):
            op.append(positive[i])
            op.append(negative[i])

        return op
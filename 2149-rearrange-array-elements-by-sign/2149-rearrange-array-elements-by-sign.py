class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        pos_ind = 0
        neg_ind = 1
        n= len(nums)
        op = [0]*n

        for i in nums:
            if i >= 0:
                op[pos_ind] = i
                pos_ind += 2
            else:
                op[neg_ind] = i
                neg_ind +=2

        return op
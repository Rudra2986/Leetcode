class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        sum_arr = []
        sum = 0
        for i in nums:
            sum += i
            sum_arr.append(sum)

        total_sum = sum_arr[-1]
        ls = 0
        rs = 0

        for i in range(0,len(nums)):

            if i > 0:
                ls = sum_arr[i-1]
            else:
                ls = 0
            rs = total_sum - sum_arr[i]

            if ls == rs :
                return i

        return -1
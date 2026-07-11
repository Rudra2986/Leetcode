class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        final = 0

        for i in nums:
            if i == 1:
                max_count += 1
                if final < max_count:
                    final = max_count
            else:
                if final > max_count:
                    max_count = 0
                else : 
                    final = max_count
                    max_count = 0

        return final
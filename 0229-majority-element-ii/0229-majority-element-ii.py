class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        freq = {}
        n = len(nums)
        
        op = []

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        

        for i in freq:
            if freq[i] > n//3:
                op.append(i)
        
        return op
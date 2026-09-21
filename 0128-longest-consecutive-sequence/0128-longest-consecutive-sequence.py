class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        n = len(nums)
        if n == 0: return 0

        longest = 1
        NumsSet = set(nums)

        for i in NumsSet:

            if (i-1) not in NumsSet:
                current = i
                curr_streak = 1

                while (current + 1) in NumsSet:
                    current += 1
                    curr_streak += 1
                
                longest = max(curr_streak, longest)
        
        return longest

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

# [-2,1,-3,4,-1,2,1,-5,4]
        for i in range(1, len(nums)):
            # Decide:
            # Continue previous subarray: current_sum + nums[i]
            # OR
            # Start fresh: nums[i]  
            if current_sum + nums[i] <  nums[i]:
                current_sum = nums[i]
            else :
                current_sum += nums[i]
            
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
            # Then update max_sum
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        op = []
        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                op.append(l+1)
                op.append(r+1)
                break
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return op
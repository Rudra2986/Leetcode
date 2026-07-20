# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while l <= r :
            mid = l + (r-l) // 2

            if isBadVersion(mid) == True:
                if isBadVersion(mid-1) == False:
                    return mid
                else:
                    r = mid - 1

            else:
                l = mid + 1
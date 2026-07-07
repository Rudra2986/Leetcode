class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        z = x
        y = 0
        while(z != 0):
            y = y*10 + (z%10)
            z = int(z/10)
        if x == y:
            return True
        return False
    
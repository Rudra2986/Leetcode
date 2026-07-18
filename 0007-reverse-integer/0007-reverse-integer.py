class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            temp = -x
        else:
            temp = x
        op = 0
        while temp != 0:
            digit = temp % 10
            op = (op * 10) + digit
            temp = temp // 10
        if (op > (2**31)-1) or (-op < -(2**31)) :
            return 0
        elif x < 0:
            return -op
        return op
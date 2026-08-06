class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        i = n
        while True:
            
            temp = i
            product = 1
            while temp > 0 :

                last = temp % 10
                product *= last
                temp = temp // 10


            if product % t == 0:
                return i
            else:
                i += 1

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num//i:
                    divisors.append(num // i)

        d_sum = 0
        for i in divisors:
            if i != num:
                d_sum += i
        
        if d_sum == num:
            return True
        else:
            return False
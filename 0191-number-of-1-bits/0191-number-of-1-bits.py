class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        
        one_counter = 0
        for i in binary:
            if i == '1':
                one_counter += 1

        return one_counter
        

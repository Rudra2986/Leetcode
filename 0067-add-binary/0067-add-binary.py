class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a,2)
        int_b = int(b,2)
        sol = int_a + int_b
        final = bin(sol)
        final = final[2:]
        
        return final
    
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        op = ""
        balance = 0


# Input: s = "(()())(())"
# Output:    "()()()"


        for i in s:
            if i == "(":
                if balance != 0:
                    op += i
                balance += 1
                
            else:
                balance -= 1
                if balance != 0:
                    op += i
        return op
class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        curr = ''

        for i in s:

            if i == '(' or i == '[' or i == '{':
                stack.append(i)
                curr = i

            else:

                if len(stack) == 0:
                    return False
                if stack[-1] != pairs[i]:
                    return False
                
                stack.pop()

        return len(stack) == 0
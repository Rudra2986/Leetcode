class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        test = s
        for i in range(len(s)):

            if test == goal:
                return True

            test = test[1:] + test[0]

        return False
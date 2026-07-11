class Solution:
    def reverseString(self, s: list[str]) -> None:
        first = 0
        last = len(s)-1
        for i in range((len(s)//2)):
            s[first], s[last] = s[last], s[first]
            first += 1
            last -=1
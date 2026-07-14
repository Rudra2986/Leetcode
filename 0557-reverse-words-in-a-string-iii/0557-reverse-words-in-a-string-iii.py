class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        arr = []
        for word in words:
            word = word[::-1]
            arr.append(word)

        new_s = ''
        for i in arr:
            new_s += i
            new_s += " "
        
        new_s = new_s[:-1]
        return new_s
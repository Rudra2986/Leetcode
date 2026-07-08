class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_counter = 0
        started = False
        for i in range(len(s)-1,-1,-1):
            if (s[i] == " ") and (started == True):
                break
            elif( s[i] != " "):
                word_counter += 1
                started = True
            else:
                continue
        return word_counter
class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_s = ""
        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch
        new = clean.lower()

        for i in range(len(new) - 1, -1, -1):
            reverse_s += new[i]
        if reverse_s == new :
            return True
        return False
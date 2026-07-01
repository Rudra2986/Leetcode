class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_add = ""
        for ch in address:
            if ch == ".":
                new_add += "[.]"
            else:
                new_add += ch
        return new_add
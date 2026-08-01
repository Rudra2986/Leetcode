class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # strs = ["flower","flow","flight"]
        op = ""
        ptr = 0
        for i in strs[0]:
            for j in range(1,len(strs)):
                if ptr >= len(strs[j]):
                    return op
                if i == strs[j][ptr]:
                    continue
                else:
                    return op
            op += i
            ptr += 1
        return op
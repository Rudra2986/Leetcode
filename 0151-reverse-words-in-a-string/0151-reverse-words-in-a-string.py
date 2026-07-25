class Solution:
    def reverseWords(self, s: str) -> str:
        cleaned = s.strip()
        op = []
        final = ""
        word = ""

        for i in cleaned:
            if i == " ":
                if word != "":
                    op.append(word)
                word = ""
            else:
                word+=i

        op.append(word)


        for i in range(len(op)-1,-1,-1):
            final += op[i]
            final += " "
        return " ".join(op[::-1])
class Solution:
    def reverseWords(self, s: str) -> str:
        cleaned = s.strip()
        op = []
        word = ""

        for i in cleaned:
            if i == " ":
                if word != "":
                    op.append(word)
                word = ""
            else:
                word+=i

        op.append(word)

        return " ".join(op[::-1])
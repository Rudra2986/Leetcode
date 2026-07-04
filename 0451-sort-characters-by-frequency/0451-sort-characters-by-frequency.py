class Solution:
    def frequencySort(self, s: str) -> str:

        freq = {}
        pairs = []
        final_s = ""

        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in freq:
            pairs.append((i,freq[i]))

        pairs.sort(key=lambda pair: pair[1], reverse=True)

        for i in pairs:
                final_s += (i[0] * i[1])

        return final_s
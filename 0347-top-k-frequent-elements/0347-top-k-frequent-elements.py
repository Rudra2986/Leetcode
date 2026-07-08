class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        freq = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)
        oplist = []
        for i in range(0,k):
            oplist.append(freq[i][0])
        return oplist
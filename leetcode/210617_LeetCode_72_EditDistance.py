class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]

        for j in range(len(word2) + 1):
            d[j][0] = j

        for i in range(len(word1) + 1):
            d[0][i] = i

        for j in range(1, len(word2) + 1):
            for i in range(1, len(word1) + 1):
                if word1[i-1] == word2[j-1]:
                    d[j][i] = d[j-1][i-1]
                else:
                    d[j][i] = 1 + min(d[j-1][i],
                                    d[j][i-1],
                                    d[j-1][i-1])

        return d[j][i]

a = Solution()
print(a.minDistance('intention', 'execution'))
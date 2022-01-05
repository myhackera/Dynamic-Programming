class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        r = s[::-1]
        n = len(s)
        table = [[0]*(n+1) for i in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    table[i][j] = 0
                elif s[i-1] == r[j-1]:
                    table[i][j] = 1+table[i-1][j-1]
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        return table[n][n]

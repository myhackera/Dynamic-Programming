#User function Template for python3

class Solution:
    def lcs(self, X, Y, m, n):
        L = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    L[i][j] = 1 + L[i-1][j-1]
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        return L[m][n]
        
        
    def shortestCommonSupersequence(self, X, Y, m, n):
        return m+n-self.lcs(X, Y, m, n)

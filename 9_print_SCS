class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        
        L = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif str1[i-1] == str2[j-1]:
                    L[i][j] = 1 + L[i-1][j-1]
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        # print(L)
        i = m
        j = n
        s = ""
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                s += str1[i-1]
                i -= 1
                j -= 1
            else:
                if L[i-1][j] > L[i][j-1]:
                    s += str1[i-1]
                    i -= 1
                else:
                    s += str2[j-1]
                    j -= 1
        
        while i > 0:
            s += str1[i-1]
            i -= 1
        while j > 0:
            s += str2[j-1]
            j -= 1
        
        # print(s)
        s = s[::-1]
        return s

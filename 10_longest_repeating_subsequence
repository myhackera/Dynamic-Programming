#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, str):
		a = str
		b = str
		m = n = len(a)
		
		L = [[0 for j in range(n+1)] for i in range(m+1)]
		
		for i in range(m+1):
		    for j in range(n+1):
		        if i == 0 or j == 0:
		            L[i][j] = 0
		        elif a[i-1] == b[j-1] and i != j:
		            L[i][j] = 1 + L[i-1][j-1]
		        else:
		            L[i][j] = max(L[i-1][j], L[i][j-1])
		return L[m][n]
		            

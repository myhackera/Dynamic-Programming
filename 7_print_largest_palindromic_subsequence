
def lcs_(X, Y) :
	
	m = len(X)
	n = len(Y)

	L = [[0] * (n + 1)] * (m + 1)

	for i in range(n + 1) :
	
		for j in range(n + 1) :
	
			if (i == 0 or j == 0) :
				L[i][j] = 0;
			elif (X[i - 1] == Y[j - 1]) :
				L[i][j] = L[i - 1][j - 1] + 1;
			else :
				L[i][j] = max(L[i - 1][j],
							L[i][j - 1])
	index = L[m][n];

	lcs = ["\n "] * (index + 1)
  
	i, j= m, n
	
	while (i > 0 and j > 0) :
	
		if (X[i - 1] == Y[j - 1]) :
			lcs[index - 1] = X[i - 1]
			i -= 1
			j -= 1
			index -= 1
      
		elif(L[i - 1][j] > L[i][j - 1]) :
			i -= 1
			
		else :
			j -= 1
	
	ans = ""
	
	for x in range(len(lcs)) :
		ans += lcs[x]
	
	return ans

def longestPalSubseq(string) :
	
	# Find reverse of str
	rev = string[: : -1]
	
	# Return LCS of str and its reverse
	return lcs_(string, rev)

# Driver Code
if __name__ == "__main__" :

	string = "GEEKSFORGEEKS";
	print(longestPalSubseq(string))


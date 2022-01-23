def lcSubstr(x, y, m, n):
    
    L = [[0 for i in range(n+1)] for j in range(m+1)]
    
    result = 0
    
    for i in range(m + 1):
        for j in range(n + 1):
            
            if (i == 0 or j == 0):
                L[i][j] = 0
                
            elif (X[i-1] == Y[j-1]):
                L[i][j] = L[i-1][j-1] + 1
                result = max(result, L[i][j])
                
            else:
                L[i][j] = 0
                
    return print(result)
                
           
if __name__ == "__main__":
    X = "OldSite:GeeksforGeeks.org"
    Y = "NewSite:GeeksQuiz.com"
    m = len(X)
    n = len(Y)
 
    lcSubstr(X, Y, m, n)

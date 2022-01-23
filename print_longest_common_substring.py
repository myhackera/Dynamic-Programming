def printLCSSubStr(x, y, m, n):
    
    L = [[0 for i in range(n + 1)]
                 for j in range(m + 1)]
    
    large = 0
    row = col = 0
    
    for i in range(m+1):
        for j in range(n+1):
            
            if i == 0 or j == 0:
                L[i][j] = 0
                
            elif x[i-1] == y[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
                
                if large < L[i][j]:
                    large = L[i][j]
                    row = i 
                    col = j 
            else:
                L[i][j] = 0
    
    print(L)
    res = ['0']*large
    
    while L[row][col] != 0:
        large -= 1 
        res[large] = x[row-1]
        row -= 1 
        col -= 1 
        
    return print(''.join(res))
        

if __name__ == "__main__":
    X = "OldSite:GeeksforGeeks.org"
    Y = "NewSite:GeeksQuiz.com"
    m = len(X)
    n = len(Y)
 
    printLCSSubStr(X, Y, m, n)

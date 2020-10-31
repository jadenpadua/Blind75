n = 5

def printSubMatricesSizekxk(mat, k):

    for i in range(n - k + 1):
        for j in range(n - k + 1):
            
            submatrix = []
            for p in range(i, k + i):
                row = []
                for q in range(j, k + j):
                    row.append(mat[p][q])
                
                submatrix.append(row)
            
            print(submatrix)

printSubMatricesSizekxk(
    
[[1, 1, 1, 1, 1], 
[2, 2, 2, 2, 2], 
[3, 3, 3, 3, 3], 
[4, 4, 4, 4, 4], 
[5, 5, 5, 5, 5]], 3 )

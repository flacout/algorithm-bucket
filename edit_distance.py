# Uses python3
def edit_distance(A, B):
    n=len(A)+1
    m=len(B)+1
    mat = [[0]*m for i in range(n)]
    for i in range(n) : mat[i][0] = i
    for j in range(m) : mat[0][j] = j
    
    for j in range(1,m):
        for i in range(1,n):
            insertion = mat[i][j-1] + 1
            deletion = mat[i-1][j] +1
            match = mat[i-1][j-1]
            mismatch = mat[i-1][j-1] +1
            if A[i-1] == B[j-1] : mat[i][j] = min(insertion, deletion, match)
            else : mat[i][j] = min(insertion, deletion, mismatch)
    return mat[n-1][m-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))

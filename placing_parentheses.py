# Uses python3
def evalt(a, b, op):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)
    else:
        assert False


def get_maximum_value(dataset):
    numbers = list(dataset[::2])
    operators = list(dataset[1::2])
    n = len(numbers)
    global m, M
    m = [[0]*n for i in range(n)]
    M = [[0]*n for i in range(n)]
    for i in range(n):
        m[i][i] = numbers[i]
        M[i][i] = numbers[i]
    # traverse matrix, diagonal after diagonal
    # fill max and min values in max and min matrices
    for s in range(1,n):
        for i in range(n-s):
            j = i+s
            m[i][j], M[i][j] = minAndMax(i, j, operators)
    return M[0][n-1]

def minAndMax(i, j, operators):
    mini = float("inf")
    maxi = -float("inf")
    for k in range(i,j):
        a = evalt(M[i][k], M[k+1][j], operators[k])
        b = evalt(M[i][k], m[k+1][j], operators[k])
        c = evalt(m[i][k], M[k+1][j], operators[k])
        d = evalt(m[i][k], m[k+1][j], operators[k])
        mini = min(mini,a,b,c,d)
        maxi = max(maxi,a,b,c,d)
    return(mini, maxi)


if __name__ == "__main__":
    print(get_maximum_value(input()))

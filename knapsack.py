# Uses python3
import sys 

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def knapsack(W, n,  weights):
    values = [[0]*(W+1) for i in range(n+1)] 
    for i in range(1, (n+1)):
        for w in range(1, (W+1)):
            values[i][w] = values[i-1][w]
            if weights[i-1] <= w:
                val = values[i-1][w-weights[i-1]] + weights[i-1]
                if values[i][w] < val : values[i][w] = val 
    return values[n][W]
'''
W=10
n=3
weights = [1,4,8]
print (knapsack(W,n,weights))
W=1
n=3
weights = [1,4,8]
print (knapsack(W,n,weights))
W=1
n=3
weights = [2,4,8]
print (knapsack(W,n,weights))
W=10
n=4
weights = [0,4000,8,2]
print (knapsack(W,n,weights))'''

input = sys.stdin.read()
W, n, *weights = list(map(int, input.split()))
print (knapsack(W,n,weights))

'''if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))'''

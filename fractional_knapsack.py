# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    return value

def get_optimal_value2(capacity, weights, values):
    # sort all list based on ratio.
    ratio = [values[i]/weights[i] for i in range(len(values))]
    sortedList = sorted(zip(ratio,values,weights), reverse=True)
    vs=[]
    ws=[]
    rs=[]
    for a,b,c in sortedList:
        vs.append(b)
        ws.append(c)
        rs.append(a)

    # knapsack algo
    V =0
    for i in range(len(vs)):
        if capacity==0 : return V
        a = min(ws[i], capacity)
        V+= a*rs[i]
        capacity-= a
    return V


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value2(capacity, weights, values)
    print("{:.10f}".format(opt_value))

'''
v = [60,100,120]
w = [20,50,30]
print(get_optimal_value2(50, w, v))
v = [500]
w = [30]
print(get_optimal_value2(10, w, v))'''

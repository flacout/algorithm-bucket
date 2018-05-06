# Uses python3
import sys

def binary_search(a, left, right, x):
    #left, right = 0, len(a)-1
    if left > right : return -1

    mid = (right-left)//2  + left
    if x == a[mid] : return mid
    elif x < a[mid] : return binary_search(a, left, mid-1,  x)
    else : return binary_search(a, mid+1, right, x) 

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, 0, len(a)-1,  x), end = ' ')

'''
a = [1,5,8,8,12,13]
xs = [8,1,23,1,11,13]
for x in xs:
	print(binary_search(a, 0, len(a)-1, x), end=' ')'''

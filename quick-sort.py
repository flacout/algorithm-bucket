# Uses python3
import sys
import random

# m1 mark the first pivot number
# m2 mark one after the last pivot number
def partition3(a, l, r):
    x = a[l]
    m1, m2 = l, l+1
    for i in range(l+1, r+1):
        if a[i] < x :
            a[m2], a[i] = a[i], a[m2]
            a[m1], a[m2] = a[m2], a[m1]
            m1 += 1
            m2 += 1
        elif a[i]==x :
            a[m2], a[i] = a[i], a[m2]
            m2+=1
    return m1, m2

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1,m2 = partition3(a, l, r)
    #m = partition2(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

'''
a = [2,6,443,7,5,1]
print(a)
randomized_quick_sort(a, 0, 5)
for x in a:
    print(x, end=' ')

a = [2,6,443,2,2,1]
print(a)
randomized_quick_sort(a, 0, 5)
for x in a:
    print(x, end=' ')

a = [2,2,2,2,2]
print(a)
randomized_quick_sort(a, 0, 4)
for x in a:
    print(x, end=' ')

a = [2,1,443,2,2,1]
print(a)
randomized_quick_sort(a, 0, 5)
for x in a:
    print(x, end=' ')

a = [2,2,0,443,2,2,1]
print(a)
randomized_quick_sort(a, 0, 6)
for x in a:
    print(x, end=' ')'''
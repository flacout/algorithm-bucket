# python3
from sys import stdin
  
def solve_diet_problem(n, m, A, b, c):
    solutions = []

    # preprocessing
    for i in range(m):
        eq_positive = [-1 if j==i else 0 for j in range(m)]
        A.append(eq_positive)
        b.append(0)
    eq_infinity = [1 for i in range(m)]
    A.append(eq_infinity)
    b.append(10**9)
    # infinity index= n+m

    subset_equations = choose(list(range(n+m+1)), m)
    #print(A)
    #print(b)
    for subset in subset_equations:
        #print("subset", subset)
        vertex = solve_subset(subset, A, b)
        if vertex=='insolvable':
            continue
        if m+n in subset:
            vertex.append('inf')
        #print('vertex', vertex)
        if satisfy_inequalities(vertex, A, b, m):
            solutions.append(vertex)

    #print('solutions', solutions)
    # no solution
    if len(solutions)==0:
        return -1, 0
    solution = find_best_vertex(solutions, c)
    if solution == 'infinity':
        return 1,0
    else:
        return 0, solution



##################################################
# choose k combinaison in a list of values
#################################################
def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next
def choose(l, k):
    return list(choose_iter(l, k))


##################################################
# guaussian elimination
#################################################
def solve_subset(subset, A, b):
    a=[]
    for i in subset:
        # deep copy not references
        a.append(A[i][:])
    bb = [b[i] for i in subset]
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns, size)
        if pivot_element =='insolvable':
            return 'insolvable'
        SwapLines(a, bb, used_rows, pivot_element)
        ProcessPivotElement(a, bb, pivot_element, size)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return bb


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def SelectPivotElement(a, used_rows, used_columns, size):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    while a[pivot_element.row][pivot_element.column]==0:
        if pivot_element.column==size-1:
            return 'insolvable'
        pivot_element.column += 1

    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;

def ProcessPivotElement(a, b, pivot_element, size):
    # divide equation to make pivot=1
    value_pivot = a[pivot_element.row][pivot_element.column]
    #print(value_pivot)
    for i in range(size):
        a[pivot_element.row][i] /= value_pivot
    b[pivot_element.row] /= value_pivot

    # substract equation from other equations
    for i in range(size):
        # don't process pivot equation!
        if i == pivot_element.row:
            continue

        operation = a[i][pivot_element.column]
        # don't process row were xi is already 0
        if operation ==0:
            continue
        for j in range(size):
            a[i][j] += a[pivot_element.row][j]*(-operation)
        b[i] += b[pivot_element.row]*(-operation)


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True




#######################################################
# choose solution in vertices
######################################################
def satisfy_inequalities(vertex, A, b, m):
    for eq in range(len(A)):
        result = 0.0
        for i in range(m):
            result += vertex[i]*A[eq][i]
        if result>(b[eq]+0.0001):
            return False

    return True



def find_best_vertex(solutions, c):
    maximum = -float("inf")
    best_vertex=[]

    for vertex in solutions:
        sol = 0.0
        for i in range(m):
            sol += vertex[i]*c[i]
        if sol> maximum:
            maximum = sol
            best_vertex = vertex
    
    if best_vertex[-1]=='inf':
        return 'infinity'
    return best_vertex




#######################################################
# MAIN
######################################################
n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

anst, ansx = solve_diet_problem(n, m, A, b, c)

if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")


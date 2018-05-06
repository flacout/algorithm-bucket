# python3
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;

class Node:
    def __init__(self):
        self.label = 0
        self.childs = []

def height(tree, root):
    if len(tree[root].childs)==0 : return 1
    maxHeight =0
    for i in tree[root].childs :
        h = height(tree, i) + 1
        maxHeight = max(h, maxHeight)
    return maxHeight

def main():
  #tree = TreeHeight()
  #tree.read()
  #print(tree.compute_height())
  
  n = int(sys.stdin.readline())
  parents = list(map(int, sys.stdin.readline().split()))
  
  tree = [Node() for i in range(n)]
  root = -1
  for child, parent in enumerate(parents):
    if parent==-1 : root = child
    else : tree[parent].childs.append(child)
  print(height(tree, root))

threading.Thread(target=main).start()

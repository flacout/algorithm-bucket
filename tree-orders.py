# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self, i):
    #self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if i == -1 : return
    self.inOrder(self.left[i])
    print(self.key[i], end=' ')
    self.inOrder(self.right[i])


  def preOrder(self, i):
    #self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if i == -1 : return
    print(self.key[i], end=' ')
    self.preOrder(self.left[i])
    self.preOrder(self.right[i])

  def postOrder(self, i):
    #self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if i == -1 : return
    self.postOrder(self.left[i])
    self.postOrder(self.right[i])
    print(self.key[i], end=' ')
                

def main():
  tree = TreeOrders()
  tree.read()
  #print(" ".join(str(x) for x in tree.inOrder()))
  #print(" ".join(str(x) for x in tree.preOrder()))
  #print(" ".join(str(x) for x in tree.postOrder()))
  tree.inOrder(0)
  print()
  tree.preOrder(0)
  print()
  tree.postOrder(0)
  print()

threading.Thread(target=main).start()

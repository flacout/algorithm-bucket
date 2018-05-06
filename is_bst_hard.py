#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def minimum(tree):
  i = 0
  while tree[i][1] != -1:
    i = tree[i][1]
  return i

def nextNode(i, tree):
  if tree[i][2] != -1 :
    if tree[i][0] == tree[ tree[i][2] ][0]: return tree[i][2], 1
    return leftDescendant(tree[i][2], tree)
  else : return rightAncestor(i, tree)

def leftDescendant(i, tree):
  if tree[i][1] == -1 : return i, 1
  else : return leftDescendant(tree[i][1], tree)

def rightAncestor(i, tree):
  if tree[ tree[i][3] ][1] == i : return tree[i][3], 0
  else : return rightAncestor(tree[i][3],tree)

def IsBinarySearchTree(tree):
  if len(tree) == 0: return True
  # Implement correct algorithm here
  nex = minimum(tree)
  directRight=0
  for i in range(len(tree)-1):
      cur = nex
      nex, directRight = nextNode(cur, tree)
      if tree[cur][0] < tree[nex][0] : continue
      if tree[cur][0] == tree[nex][0] and directRight : 
        if tree[nex][1] !=-1 : return False
        else : continue
      else : return False
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = [[0,0,0,0] for i in range(nodes)]
  for i in range(nodes):
    k, l, r = map(int, sys.stdin.readline().strip().split())
    tree[i][0] = k
    tree[i][1] = l
    tree[i][2] = r
    if l!=-1 : tree[l][3] = i
    if r!=-1 : tree[r][3] = i


  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

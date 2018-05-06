# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  # Initialization with one char suffixes.
  order = sortCharacters(text)
  classes = computeCharClasses(text, order)
  L = 1
  while L < len(text):
    order = sortDoubled(text, L, order, classes)
    classes = updateClasses(order, classes, L)
    L = 2*L
  return order

def sortCharacters(text):
  order = [0]*len(text)
  # alphabet arbitrary size 90
  count = [0]*90
  for i in range(len(text)):
    count[ord(text[i])] = count[ord(text[i])]+1
  for j in range(1,90):
    count[j] = count[j] + count[j-1]
  i = len(text)-1
  while i>=0:
    c = text[i]
    count[ord(c)] = count[ord(c)] - 1
    order[count[ord(c)]]= i
    i -=1
  #print(order)
  return order

def computeCharClasses(text, order):
    classes = [0]*len(text)
    classes[order[0]] = 0
    for i in range(1,len(text)):
      if text[order[i]] != text[order[i-1]]:
        classes[order[i]] = classes[order[i-1]]+1
      else:
        classes[order[i]] = classes[order[i-1]]
    #print(classes)
    return classes

def sortDoubled(text, L, order, classes):
  # now classes is like the new string
  count = [0]*len(text)
  newOrder = [0]*len(text)

  for i in range(len(text)):
    count[classes[i]] = count[classes[i]]+1
  for j in range(1,len(text)):
    count[j] = count[j] + count[j-1]

  i = len(text)-1
  while i>=0:
    # startindex of double
    start = (order[i]-L+len(text)) % len(text)
    cl = classes[start]
    count[cl] = count[cl]-1
    newOrder[count[cl]] = start
    i -=1
  return newOrder


def updateClasses(order, classes, L):
  n = len(order)
  newClass = [0]*n
  newClass[order[0]] = 0
  for i in range(1, n):
    cur = order[i]
    prev = order[i-1]
    mid = (cur+L) %n
    midPrev = (prev+L) %n
    if (classes[cur] != classes[prev]) or (classes[mid] != classes[midPrev]):
      newClass[cur] = newClass[prev]+1
    else:
      newClass[cur] = newClass[prev]
  return newClass



if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))

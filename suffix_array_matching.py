# python3
import sys

def find_occurrences(text, patterns):
    occs = set()
    text = text+'$'

    suffix_array = build_suffix_array(text)
    starts, occ_counts_before, bwt = PreprocessBWT(text, suffix_array)
    occurrence_counts = []
    for pattern in patterns:
      occurrence_counts=(CountOccurrences(pattern, bwt, starts, occ_counts_before, suffix_array))
      for i in occurrence_counts:
        occs.add(i)

    return occs


def CountOccurrences(pattern, bwt, starts, occ_counts_before, suffix_array):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  #         0$ 1A 2T 3G 4C
  letters = {'$':0, 'A':1, 'T':2, 'G':3, 'C':4}
  top=0
  bottom = len(bwt)-1
  matches_index = []
  while True:
    if len(pattern)!=0:
      char = pattern[-1]
      j = letters[char]
      pattern = pattern[:-1]
      found=False
      for i in range(top,bottom+1):
        if bwt[i] == char:
          top = occ_counts_before[i][j] + starts[char] -1
          bottom = occ_counts_before[bottom][j] + starts[char] -1
          found = True
          break

      if found==False:
        return matches_index
    # when pattern is finished proccessing
    else:
        for i in range(top, bottom+1):
            matches_index.append(suffix_array[i])
        return matches_index

  return matches_index


def PreprocessBWT(bwt, suffix_array):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  # Implement this function yourself
  lastCol = ['']*len(suffix_array)
  for i in range(len(suffix_array)):
    if suffix_array[i] == 0:
      lastCol[i] = '$'
    else:
      lastCol[i] = text[suffix_array[i]-1]
  counts, lastCol2 = MakeCounts(lastCol)
  indexes = MakeIndex(counts)
  return indexes, lastCol2, lastCol

def MakeCounts(lastCol):
    #         0$ 1A 2T 3G 4C
    counts = [0,  0, 0, 0, 0]
    lastCol2 = []
    for c in lastCol:
        if c=='A': 
            counts[1]+= 1
            lastCol2.append([counts[0], counts[1],counts[2],counts[3],counts[4]])
        elif c=='T': 
            counts[2]+=1
            lastCol2.append([counts[0], counts[1],counts[2],counts[3],counts[4]])
        elif c=='G': 
            counts[3]+=1
            lastCol2.append([counts[0], counts[1],counts[2],counts[3],counts[4]])
        elif c=='C': 
            counts[4]+=1
            lastCol2.append([counts[0], counts[1],counts[2],counts[3],counts[4]])
        elif c=='$': 
            counts[0]+=1
            lastCol2.append([counts[0], counts[1],counts[2],counts[3],counts[4]])

    return counts, lastCol2

def MakeIndex(counts):
    indexDollar = 0
    indexA = 0
    indexT = 0
    indexG = 0
    indexC = 0
    # A
    if counts[1]!=0:
        indexA = 1
    # C
    if counts[4]!=0 and indexA!=0:
        indexC = 1+counts[1]
    elif counts[4]!=0 :
        indexC = 1
    # G
    if counts[3]!=0 and indexC!=0:
        indexG = indexC+counts[4]
    elif counts[3]!=0 and indexA!=0:
        indexG = 1+counts[1]
    elif counts[3]!=0:
        indexG = 1
    # T
    if counts[2]!=0 and indexG!=0:
        indexT = indexG+counts[3]
    elif counts[2]!=0 and indexC!=0:
        indexT = indexC+counts[4]
    elif counts[2]!=0 and indexA!=0:
        indexT = 1+counts[1]
    elif counts[2]!=0:
        indexT = 1

    indexes = {'$':indexDollar, 'A':indexA, 'T':indexT, 'G':indexG, 'C':indexC}
    return indexes


##################################################################
#SUFFIX array
##################################################################
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
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))
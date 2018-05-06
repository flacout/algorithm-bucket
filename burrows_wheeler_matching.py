# python3
import sys


def PreprocessBWT(bwt):
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
  lastCol = [c for c in bwt]
  firstCol = sorted(lastCol)
  #print(firstCol)
  counts, lastCol2 = MakeCounts(lastCol)
  indexes = MakeIndex(counts)
  return indexes, lastCol2

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



def CountOccurrences(pattern, bwt, starts, occ_counts_before):
  """
  Compute the number of occurrences of string pattern in the text
  given only Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  #         0$ 1A 2T 3G 4C
  letters = {'$':0, 'A':1, 'T':2, 'G':3, 'C':4}
  top=0
  bottom = len(bwt)-1
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
        return 0
    # when pattern is finished proccessing
    else:
        return bottom - top + 1


  return 0
     


if __name__ == '__main__':
  bwt = sys.stdin.readline().strip()
  pattern_count = int(sys.stdin.readline().strip())
  patterns = sys.stdin.readline().strip().split()
  # Preprocess the BWT once to get starts and occ_count_before.
  # For each pattern, we will then use these precomputed values and
  # spend only O(|pattern|) to find all occurrences of the pattern
  # in the text instead of O(|pattern| + |text|).  
  starts, occ_counts_before = PreprocessBWT(bwt)
  #for l in occ_counts_before:
  #  print(l)
  occurrence_counts = []
  for pattern in patterns:
    occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
  print(' '.join(map(str, occurrence_counts)))

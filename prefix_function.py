# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  S = pattern + '$' + text
  borders = prefixFunction(S)
  #print (S)
  #print(borders)
  result = []
  for i in range(len(pattern),len(S)):
    if borders[i] == len(pattern):
        result.append(i-2*len(pattern))
  return result


def prefixFunction(P):
  s=[0]*len(P)
  border = 0

  for i in range(1,len(P)):
    while (border>0) and (P[i]!=P[border]):
        border = s[border-1]
    if P[i] == P[border]:
        border = border+1
    else:
        border = 0
    s[i] = border
  return s


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))


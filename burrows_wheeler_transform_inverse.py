# python3
import sys

def MakeCounts(lastCol):
    #         0$ 1A 2T 3G 4C
    counts = [0,  0, 0, 0, 0]
    lastCol2 = []
    for c in lastCol:
        if c=='A': 
            counts[1]+= 1
            lastCol2.append((c,counts[1]))
        elif c=='T': 
            counts[2]+=1
            lastCol2.append((c,counts[2]))
        elif c=='G': 
            counts[3]+=1
            lastCol2.append((c,counts[3]))
        elif c=='C': 
            counts[4]+=1
            lastCol2.append((c,counts[4]))
        elif c=='$': 
            counts[0]+=1
            lastCol2.append((c,counts[0]))

    return counts, lastCol2


def InverseBWT(bwt):
    lastCol = [c for c in bwt]
    firstCol = sorted(lastCol)
    counts, lastCol2 = MakeCounts(lastCol)
    #print(firstCol)
    #print(lastCol)
    #print(lastCol2)
    #print(counts)

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

    #print(indexA)
    #print(indexC)
    #print(indexG)
    #print(indexT)

    reversedString='$'
    index=0
    for i in range(len(bwt)-1):
        char = lastCol[index]
        reversedString+= char

        if char=='A':
            index = lastCol2[index][1] + indexA -1
        elif char=='T':
            index = lastCol2[index][1] + indexT -1
        elif char=='G':
            index = lastCol2[index][1] + indexG -1
        elif char=='C':
            index = lastCol2[index][1] + indexC -1


    return reversedString[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
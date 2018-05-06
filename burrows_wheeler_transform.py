# python3
import sys

def BWT(text):
    mat = [text]
    for i in range(1,len(text)):
        mat.append(text[-i:]+text[0:-i])
    mat.sort()
    transform = ''
    for w in mat:
        transform += w[-1]

    return transform

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
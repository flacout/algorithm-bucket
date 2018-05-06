# python3
import sys

NA = -1

class Node:
    def __init__ (self):
        #self.next = [NA] * 4
        self.next = {}
        self.patternEnd = False


def makeTree(patterns):
    root = Node()
    # for each pattern
    for pattern in patterns:
        node = root
        # for each char in the pattern
        for i in range(len(pattern)):
            c = pattern[i]
            if c in node.next:
                # go to the branching node
                node = node.next[c]
                if i==len(pattern)-1:
                    node.patternEnd = True
            else:
                # create new node, and append it to child of current node
                node.next[c] = Node()
                # go to this new node
                node = node.next[c]
                if i==len(pattern)-1:
                    node.patternEnd = True
    return root

def solve (text, n, patterns):
    result = []
    root = makeTree(patterns)

    for pos in range(len(text)):
        node = root
        for i in range(pos, len(text)):
            char=text[i]
            if char in node.next:
                node = node.next[char]
                if node.patternEnd == True:
                        result.append(pos)
                        break
            else: break

    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)
ans.sort()

sys.stdout.write (' '.join (map (str, ans)) + '\n')

# python3
import sys

NA = -1

class Node:
    def __init__ (self):
        # indexing in array: 0:A, 1:T, 2:G, 3:C
        #self.next = [NA] * 4
        self.next = {}

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
            else:
                # create new node, and append it to child of current node
                node.next[c] = Node()
                # go to this new node
                node = node.next[c]
    return root


# slide the tree at every position of the TEXT
def solve (text, n, patterns):
    result = []
    root = makeTree(patterns)

    for pos in range(len(text)):
        node = root
        for i in range(pos, len(text)):
            char=text[i]
            if char in node.next:
                node = node.next[char]
                if len(node.next) == 0:
                        result.append(pos)
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

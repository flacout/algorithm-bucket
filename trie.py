#Uses python3
import sys


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    val=0
    root=0
    tree[root] = {}
    for pattern in patterns:
        node = root
        for i in range(len(pattern)):
            c = pattern[i]
            if c in tree[node]:
                # go to the branching node
                node = tree[node][c]
            else:
                # create new node (dict) 
                val += 1
                tree[val] = {}
                # append this child to current node
                tree[node][c] = val
                # go to this new node
                node = val
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

# other implementation possible with 
# node class
# attribute value(int) and childs{'char':int}
# traverse deepth first

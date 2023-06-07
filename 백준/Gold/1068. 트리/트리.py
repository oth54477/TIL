import sys
from collections import deque

input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.parent = None
        self.children = []
        self.number = data


N = int(input().strip())

tree = list(map(int, input().strip().split()))

M = int(input().strip())

tree_dict = dict()

tree_dict[-1] = Node(-1)

for i, p in enumerate(tree):
    if i in tree_dict:
        node = tree_dict[i]
    else:
        node = Node(i)
    if p not in tree_dict:
        tree_dict[p] = Node(p)
    node.parent = tree_dict[p]
    tree_dict[p].children.append(node)
    tree_dict[i] = node

dq = deque([-1])

count = 0

while dq:
    n = dq.popleft()
    if n != M:
        if n in tree_dict and tree_dict[n].children:
            for child in tree_dict[n].children:
                if child.number != M:
                    dq.append(child.number)
                elif len(tree_dict[n].children) == 1:
                    count += 1

        else:
            count += 1

if n == -1:
    count = 0

print(count)

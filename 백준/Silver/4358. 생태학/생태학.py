import sys
from collections import defaultdict
input = sys.stdin.readline

tree_dict = defaultdict(int)
total_count = 0

while True:
    tree = input().strip()
    if tree == "":
        break
    total_count += 1
    tree_dict[tree] += 1

for tree_name in sorted(tree_dict.keys()):
    print(tree_name, "%.4f" %((tree_dict[tree_name] / total_count) * 100))
import sys
from itertools import combinations

input = sys.stdin.readline

arr = list(map(str, input().strip()))
stack = []
tuples = []
result = set()
for idx, value in enumerate(arr):
    if value == '(':
        stack.append(idx)
    elif value == ')':
        tuples.append((stack.pop(), idx))
for i in range(1, len(tuples) + 1):
    for case in combinations(tuples, i):
        temp = set()
        for a,b in case:
            temp.add(a)
            temp.add(b)
        string = ''
        for j, v in enumerate(arr):
            if j not in temp:
                string += v
        result.add(string)
print(*sorted(result), sep='\n')



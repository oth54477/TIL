import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
arr = [list(map(lambda x: tuple(map(int, x)) if len(x) == 3 else int(x), input().split())) for _ in range(n)]

result = set()

for case in permutations(range(1, 10), 3):
    for i in arr:
        number, strike, ball = i
        s, b = 0, 0
        for idx, m in enumerate(number):
            if m == case[idx]:
                s += 1
            elif m in case:
                b += 1
        if strike != s or ball != b:
            break
    else:
        result.add(case)
        continue

print(len(result))
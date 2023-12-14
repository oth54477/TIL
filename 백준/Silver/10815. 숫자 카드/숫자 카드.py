import sys
input = sys.stdin.readline

N = int(input().strip())
card_set = set(map(int, input().strip().split()))
M = int(input().strip())
arr = list(map(int, input().strip().split()))

result = []
for i in arr:
    if i in card_set:
        result.append(1)
    else:
        result.append(0)
print(*result)
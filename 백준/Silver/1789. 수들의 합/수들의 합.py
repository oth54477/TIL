import sys
input = sys.stdin.readline

S = int(input().strip())

s = S
result = 0
for i in range(1, S+1):
    s -= i
    result += 1
    if s == 0:
        break
    if s <= i:
        break
print(result)
import sys
input = sys.stdin.readline

n = int(input())
cnt = -1

k = n // 5
for i in range(k, -1, -1):
    a = (n - 5 * i)
    if a % 3 == 0:
        cnt = i + a // 3
        break
print(cnt)

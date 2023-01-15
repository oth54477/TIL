import sys
input = sys.stdin.readline


n, m = map(int, input().strip().split())

numbers = list(map(int, input().strip().split()))
temp = 0
sums = [0]
for i in numbers:
    temp += i
    sums.append(temp)
for j in range(m):
    s, e = map(int, input().strip().split())
    print(sums[e] - sums[s-1])

import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(lambda x: int(x) if x.isdigit() else x, input().strip().split())) for _ in range(n)]
for i in sorted(a, key=lambda x: x[0]):
    print(*i)





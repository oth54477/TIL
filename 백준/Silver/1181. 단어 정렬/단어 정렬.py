import sys
input = sys.stdin.readline

n = int(input())

s = set()
for _ in range(n):
    s.add(input().strip())

print(*sorted(sorted(s), key=len),sep='\n')
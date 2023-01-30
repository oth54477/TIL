import sys

input = sys.stdin.readline

T = int(input().strip())

for t in range(1, T+1):
    a, b = map(int, input().strip().split())
    print(f'Case #{t}: {a} + {b} = {a + b}')
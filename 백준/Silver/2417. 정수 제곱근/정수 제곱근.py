import sys
input = sys.stdin.readline

N = int(input().strip())

result = int(N**(1/2))
if result**2 >= N:
    result = result
else:
    result = result + 1

print(result)
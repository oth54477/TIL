import sys
input = sys.stdin.readline

n = int(input().strip())
drinks = list(map(int, input().strip().split()))

drinks.sort()

result = 0
for drink in drinks[:-1]:
    result += drink/2
result += drinks[-1]

print(result)
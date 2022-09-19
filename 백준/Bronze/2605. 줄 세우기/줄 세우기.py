n = int(input())
number = list(map(int, input().split()))

result = []
for i in range(n):
    result.insert(i - number[i], i + 1)
print(*result)

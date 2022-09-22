a = [1, 1, 2, 2, 2, 8]
b = list(map(int, input().split()))

for x, y in zip(a, b):
    print(x-y, end=' ')
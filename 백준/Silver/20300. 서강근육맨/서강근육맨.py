import sys
input = sys.stdin.readline

n = int(input().strip())
values = list(map(int, input().strip().split()))

values.sort()
max_value = 0
if n % 2 == 0:
    for i in range(n//2):
        temp = values[i] + values[n-i-1]
        if temp > max_value:
            max_value = temp
else:
    for i in range(n//2):
        temp = values[i] + values[n-i-2]
        if temp > max_value:
            max_value = temp
print(max_value)
import sys

input = sys.stdin.readline

n = int(input())
result = 1
while n > 1:
    result *= n
    n -= 1
count = 0
for i in str(result)[::-1]:
    if i == '0':
        count += 1
    else:
        break
print(count)

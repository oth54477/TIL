import sys
input = sys.stdin.readline

n = int(input().strip())
m = n//5
while m > 0:
    if (n - (5 * m)) % 2 == 0:
        break
    else:
        m -= 1
n = (n - (5 * m))
if n % 2 == 0:
    result = n // 2 + m
else:
    result = -1
print(result)
import sys
input = sys.stdin.readline

def sum_num(num):
    s = str(num)
    sum_n = 0
    for j in s:
        sum_n += int(j)
    return sum_n + num

n = int(input())
result = 0
k = sum_num(n)
for i in range(k, 0, -1):
    r = sum_num(i)
    if r == n:
        result = i
print(result)

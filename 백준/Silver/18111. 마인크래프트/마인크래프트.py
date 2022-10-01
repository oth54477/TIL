import sys
input = sys.stdin.readline

n, m ,b = map(int, input().split())

arr = []
for _ in range(n):
    arr += list(map(int, input().split()))

sum_num = sum(arr)
r = []
min_time, max_h = 999999999, 0
for k in range(257):
    if k * n * m - sum_num <= b:
        time = 0
        for i in arr:
            if i != k:
                a = i - k
                if a < 0:
                    time += -a
                else:
                    time += a * 2
        if min_time >= time:
            if max_h <= k:
                min_time, max_h = time, k

print(min_time, max_h)



import sys
input = sys.stdin.readline

n = int(input())

i = 1
now = 1
while True:
    if now >= n:
        break
    now += 6 * i
    i += 1
print(i)
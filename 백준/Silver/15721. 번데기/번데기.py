import sys

input = sys.stdin.readline

N = int(input().strip())
T = int(input().strip())
TARGET = input().strip()

n = 1
cnt = 0
total_cnt = 0
flag = True
while flag:
    rule = "0101" + "0" * (n + 1) + "1" * (n + 1)
    for s in rule:
        total_cnt += 1
        if s == TARGET:
            cnt += 1
            if cnt == T:
                flag = False
                break
    n += 1

result = total_cnt%N - 1
print(N-1 if result < 0 else result)

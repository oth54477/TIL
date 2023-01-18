import sys
input = sys.stdin.readline
a, b = map(int, input().strip().split())
cnt = 1
while True:
    s = str(b)
    if s[-1] == '1':
        if s == '1':
            result = -1
            break
        b = int(s[:-1])
        cnt += 1
        if a == b:
            result = cnt
            break
    elif b % 2 == 0:
        b //= 2
        cnt += 1
        if a == b:
            result = cnt
            break
    else:
        result = -1
        break
    
print(result)

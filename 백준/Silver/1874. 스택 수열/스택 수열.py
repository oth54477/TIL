import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
cnt = 1
result = []
breaker = False
for i in arr:
    if breaker:
        break
    while True:
        if not stack or stack[-1] < i:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        else:
            if stack[-1] == i:
                stack.pop()
                result.append('-')
                break
            else:
                print('NO')
                breaker = True
                break
else:
    print(*result,sep='\n')
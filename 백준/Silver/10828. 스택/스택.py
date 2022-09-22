import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    com, *num = map(str, input().split())

    if com == 'push':
        stack.append(num[0])
    elif com == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif com == 'size':
        print(len(stack))
    elif com == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif com == 'empty':
        if stack:
            print(0)
        else:
            print(1)
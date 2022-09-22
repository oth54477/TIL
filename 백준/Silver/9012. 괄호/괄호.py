import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    stack = []
    a = input()
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print("YES")


import sys

input = sys.stdin.readline
n = int(input())

towers = list(map(int, input().split()))
stack = []
result = []

for idx, value in enumerate(towers):
    while stack:
        if stack[-1][1] <= value:
            stack.pop()
        else:
            result.append(stack[-1][0] + 1)
            stack.append((idx, value))
            break
    else:
        result.append(0)
        stack.append((idx, value))    
        
print(*result)
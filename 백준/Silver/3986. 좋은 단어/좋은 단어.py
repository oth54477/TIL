import sys

input = sys.stdin.readline
count = 0
for _ in range(int(input())):
    word = input().strip()
    stack = []
    for s in word:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    if not stack:
        count += 1
print(count)

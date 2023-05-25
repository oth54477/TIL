def solution(s):
    stack = []
    arr = list(map(str, s))
    stack.append(arr.pop())
    l = 1
    while arr:
        stack.append(arr.pop())
        l += 1
        if l >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            l -= 2
    if stack:
        return 0
    else:
        return 1

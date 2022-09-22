import sys
input = sys.stdin.readline

while True:
    a = input().rstrip()
    if a == '.':
        break
    stack = []
    for i in a:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack.pop() != '(':
                    print('no')
                    break
            else:
                print('no')
                break
        elif i == ']':
            if stack:
                if stack.pop() != '[':
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if stack:
            print('no')
        else:
            print("yes")


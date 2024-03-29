priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1, ')': 1}
for t in range(1, 11):
    n = int(input())
    formula = input()
    postfix = ''
    stack = []
    for v in formula:
        if v.isdigit():
            postfix += v
        else:
            if stack:
                if v == ')':
                    while stack and stack[-1] != '(':
                        postfix += stack.pop()
                    stack.pop()
                elif priority[stack[-1]] >= priority[v] and v != '(':
                    while (stack and priority[stack[-1]] >= priority[v] and stack[-1] != '('):
                        postfix += stack.pop()
            if v != ')':
                stack.append(v)
    while stack:
        postfix += stack.pop()
    stack2 = []
    for e in postfix:
        if e.isdigit():
            stack2.append(int(e))
        else:
            pop1 = stack2.pop()
            pop2 = stack2.pop()
            if e == '+':
                stack2.append(pop2 + pop1)
            elif e == '-':
                stack2.append(pop2 - pop1)
            elif e == '*':
                stack2.append(pop2 * pop1)
            elif e == '/':
                stack2.append(pop2 / pop1)
    print(f'#{t} {stack2.pop()}')

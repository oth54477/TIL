def check(stack1):
    stack2 = []
    for _ in range(len(stack1)):
        pop1 = stack1.pop()
        # stack2가 비어있으면 pop1을 push
        if not stack2:
            stack2.append(pop1)
        # stack2에 값이 있으면 맨위의 값과 pop1을 비교
        else:
            # 같으면 stack2 pop
            if stack2[-1] == pop1:
                stack2.pop()
            # 다르면 pop1을 push
            else:
                stack2.append(pop1)
    print(*stack2[::-1], sep='')


for t in range(1, 11):
    n, s = map(str, input().split())
    stack = list(map(str, s))
    print(f'#{t}', end=' ')
    check(stack)

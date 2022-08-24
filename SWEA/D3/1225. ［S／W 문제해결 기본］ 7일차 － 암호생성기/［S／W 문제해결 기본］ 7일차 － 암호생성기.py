for _ in range(10):
    t = int(input())
    queue = list(map(int, input().split()))

    n = 1
    while True:
        num = queue.pop(0)
        num -= n
        if num <= 0:
            num = 0
            queue.append(num)
            break
        queue.append(num)

        n += 1
        if n == 6:
            n = 1

    print(f'#{t}', *queue)

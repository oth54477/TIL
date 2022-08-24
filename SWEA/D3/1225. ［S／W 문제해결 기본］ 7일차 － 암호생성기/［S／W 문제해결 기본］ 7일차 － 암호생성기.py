for _ in range(10):
    t = int(input())
    queue = list(map(int, input().split()))
    n = 1
    while True:
        num = queue.pop(0)
        num -= n
        if num <= 0:
            queue.append(0)
            break
        queue.append(num)
        n %= 5
        n += 1
    print(f'#{t}', *queue)

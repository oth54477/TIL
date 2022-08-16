for t in range(1, int(input()) + 1):
    a, b = map(str, input().split())
    cnt = a.count(b)
    a = a.replace(b, '')

    cnt += len(a)
    print(f'#{t} {cnt}')

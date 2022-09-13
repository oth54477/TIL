for t in range(1, int(input()) + 1):
    input()
    nums = {}

    arr = tuple(map(int, input().split()))
    r = max(arr, key=arr.count)
    print(f'#{t} {r}')
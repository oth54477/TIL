for t in range(1, int(input())+ 1):
    arr = list(map(int, input().split()))
    print(f'#{t}', round(sum(sorted(arr)[1:-1])/(len(arr) - 2)))
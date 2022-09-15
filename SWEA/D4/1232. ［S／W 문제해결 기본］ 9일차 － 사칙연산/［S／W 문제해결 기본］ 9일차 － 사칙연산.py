cal = {'+': lambda x, y: x + y,'-': lambda x, y: x - y,'*': lambda x, y: x * y,'/': lambda x, y: x // y}
for t in range(1, 11):
    n = int(input())
    arrs = [list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(n)]
    tree_arr = [0] * (n + 1)
    for arr in arrs[::-1]:
        if len(arr) == 2:
            tree_arr[arr[0]] = arr[1]
        else:
            tree_arr[arr[0]] = cal[arr[1]](tree_arr[arr[2]], tree_arr[arr[3]])
    print(f'#{t} {tree_arr[1]}')

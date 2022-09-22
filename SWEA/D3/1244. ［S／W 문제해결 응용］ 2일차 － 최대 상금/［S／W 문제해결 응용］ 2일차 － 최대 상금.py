from itertools import permutations

def change(arr, m):
    if m == n:
        result.add(int(''.join(list(map(str,arr)))))
        return 
    for case in permutations(list(range(len(arr))), 2):
        a = list(arr)
        a[case[0]], a[case[1]] = a[case[1]], a[case[0]] 
        if a not in tmp[m]:
            tmp[m].append(a)
            change(a, m+1)
        
for t in range(1, int(input()) + 1):
    info, n = map(str, input().split())
    n = int(n)
    info = list(map(int, info))
    result = set()
    tmp = [[] for _ in range(10)]
    change(info, 0)
    print(f'#{t} {max(result)}')

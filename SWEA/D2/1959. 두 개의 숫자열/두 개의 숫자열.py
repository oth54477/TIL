T=input()
for t in range(0,int(T)):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if N > M:
        N, M = M, N
        A, B = B, A

    find_max_list = []
    for i in range(0,M-N+1):
        x = 0
        for j in range(0,N):
            x = x + A[j] * B[j+i]
        find_max_list.append(x)
    print(f'#{t+1} {max(find_max_list)}')
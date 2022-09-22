def turn(n, d):
    if d == 1:
        magnets[n] = [magnets[n][-1]] + magnets[n][:-1]
    else:
        magnets[n] = magnets[n][1:] + [magnets[n][0]]

def rotation(n,d):
    visited[n] = True
    turn(n,d)
    d = -d
    if (n + 1) < 4 and status[n] and not visited[n+1]:
        rotation(n+1, d)
    if n-1 >= 0 and status[n-1] and not visited[n-1]:
        rotation(n-1, d)


for t in range(1, int(input()) + 1):
    k = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(k):
        n, d = map(int, input().split())
        n -= 1
        status = []
        visited = [False] * 4
        for i in range(3):
            if magnets[i][2] != magnets[i+1][6]:
                status.append(True)
            else:
                status.append(False)
        rotation(n,d)
    result = 0
    for score in range(4):
        result += magnets[score][0] * (2 ** score)
    print(f'#{t} {result}')


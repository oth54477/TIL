import sys
input = sys.stdin.readline




for t in range(int(input())):
    k = int(input())
    n = int(input())

    zero = list(range(n + 1))
    f = 1
    while f <= k:
        info = []
        for i in range(n + 1):
            info.append(sum(zero[:i+1]))
        zero = info
        f += 1
    print(zero[-1])

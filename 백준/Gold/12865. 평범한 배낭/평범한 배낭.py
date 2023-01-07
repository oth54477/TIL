import sys

input = sys.stdin.readline

def knapsack(W,wt,val,n):
    k = [[0 for _ in range(W+1)] for _ in range(n + 1) ]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif wt[i-1] <= w:
                k[i][w] = max(val[i-1]+ k[i-1][w-wt[i-1]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
    return k[n][W]

n, k = map(int, input().strip().split())

wt, val = [], []

for _ in range(n):
    w, v = map(int, input().strip().split())
    wt.append(w)
    val.append(v)

print(knapsack(k,wt,val,n))
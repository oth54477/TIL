def solution(n, m, x, y, r, c, k):
    import sys
    sys.setrecursionlimit(10000000)
    D = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    table = {0: "d", 1: "l", 2:"r" , 3:"u"}
    result = []
    def dfs(row, col, cnt, s):
        if result:
            return
        if cnt == k:
            if row == r and col == c:
                result.append(s)
            return
        for idx, d in enumerate(D):
            dr, dc = d
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m:
                l = abs(nr - r) + abs(nc - c)
                limit = k - (cnt-1)
                if limit >= l:
                    dfs(nr, nc, cnt+1, s + table[idx])
    x, y, r, c = x-1, y-1, r-1, c-1
    dfs(x, y, 0, "")

    if result:
        return result[0]
    else:
        return "impossible"
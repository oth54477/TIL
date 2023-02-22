import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

def make_unions():
    for r in range(N):
        for c in range(N):
            if (r, c) not in visited:
                unions.append([])
                visited.add((r, c))
                dfs(r, c)
                if unions[-1]:
                    unions[-1].append((r, c))
                else:
                    unions.pop()

def dfs(r, c):
    now_people = land[r][c]
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and (nr,nc) not in visited:
            if L <= abs(now_people - land[nr][nc]) <= R:
                unions[-1].append((nr, nc))
                visited.add((nr, nc))
                dfs(nr, nc)

def move_people(union):
    number_of_city = len(union)
    total_people = sum(map(lambda x: land[x[0]][x[1]], union))
    avr_people = total_people // number_of_city

    for city_r, city_c in union:
        land[city_r][city_c] = avr_people
        

N, L, R = map(int, input().strip().split())
land = [list(map(int, input().strip().split())) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count = 0
while True:
    visited = set()
    unions = []
    make_unions()

    if unions:
        count += 1
        for union in unions:
            move_people(union)
    else:
        break

print(count)
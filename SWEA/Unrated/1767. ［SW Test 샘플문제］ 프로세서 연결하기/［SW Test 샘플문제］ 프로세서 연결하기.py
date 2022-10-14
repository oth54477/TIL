def dfs(arr, cnt, line_cnt, now):
    global max_chip, min_line, not_connect
    # 종료조건 -> 모든 칩을 검사했을 때
    if now >= len_chip:
        if max_chip < cnt:
            max_chip = cnt
            min_line = line_cnt
            not_connect = now - cnt
        elif max_chip == cnt:
            min_line = min(min_line, line_cnt)
        return

    # 백트래킹 -> 연결에 실패환 코어 수 
    if not_connect < now - cnt:
        return

    # 현재 칩 위치 
    row, col = chips[now]

    # 상 하 좌 우 4방향 검사
    for dr, dc in dxy:
        # cell 복사
        copy_cell = [a[:] for a in arr]
        new_cnt, new_line_cnt = cnt, line_cnt
        line = []
        nr, nc = row + dr, col + dc

        # 가장자리에 도착할 때 까지 반복
        while 0 <= nr < n and 0 <= nc < n:
            # 해당 위치가 0이면
            if not copy_cell[nr][nc]:
                # 리스트에 추가
                line.append((nr, nc))
            # 0이 아니면 브레이크
            else:
                break
            # 다음 이동 위치
            nr, nc = nr + dr, nc + dc
        # 가장자리에 도착하면
        else:
            # 전선 표시하기
            for r, c in line:
                copy_cell[r][c] = 2
                new_line_cnt += 1
            # 연결된 칩 + 1
            new_cnt = cnt + 1

        # 다음 위치의 칩으로 재귀
        dfs(copy_cell, new_cnt, new_line_cnt, now + 1)


dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for tc in range(1, int(input()) + 1):
    n = int(input())
    cells = [list(map(int, input().split())) for _ in range(n)]
    connected_core = cells[0].count(1) + cells[-1].count(1)
    chips = []
    max_chip, min_line = 0, n * n
    for k in range(1, n - 1):
        connected_core += cells[k][0] + cells[k][-1]

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if cells[i][j] == 1:
                chips.append((i, j))
    len_chip = len(chips)
    not_connect = len_chip
    dfs(cells, connected_core, 0, 0)
    print(f'#{tc} {min_line}')

def chk(arr):
    for i in range(w):
        cnt, now = 0, 1
        for j in range(d):
            if arr[j][i] == now:
                cnt += 1
            else:
                now = arr[j][i]
                cnt = 1
            if cnt == k:
                break
        else:
            return False
    return True


def dfs(f_arr, chg_idx, cnt):
    global result, min_cnt

    if chk(f_arr):
        min_cnt = min(min_cnt, cnt)
        return
    if min_cnt <= cnt:
        return


    chg_idx += 1
    if chg_idx >= d:
        return
    # 염색 x
    dfs(f_arr, chg_idx, cnt)

    cnt += 1
    # 1로 염색
    arr_1 = f_arr[:]
    arr_1[chg_idx] = [1] * w
    dfs(arr_1, chg_idx, cnt)

    # 0으로 염색
    arr_0 = f_arr[:]
    arr_0[chg_idx] = [0] * w
    dfs(arr_0, chg_idx, cnt)





for tc in range(1, int(input()) + 1):
    d, w, k = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(d)]
    result, min_cnt = 0, 13
    dfs(film, -1, 0)
    print(f'#{tc} {min_cnt}')

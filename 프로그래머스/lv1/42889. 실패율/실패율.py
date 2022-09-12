def solution(N, stages):
    dict_cnt = {}
    players = len(stages)
    result = {}
    for stage in stages:
        if stage in dict_cnt:
            dict_cnt[stage] += 1
        else:
            dict_cnt[stage] = 1
    cnt = 0
    for i in range(1, N + 1):
        if i in dict_cnt:
            fail_player = dict_cnt[i]
            pass_player = players - cnt
            cnt += fail_player
            result[i] = fail_player / pass_player
        else:
            result[i] = 0

    result = sorted(result, key=lambda x: result[x], reverse=True)
    return result
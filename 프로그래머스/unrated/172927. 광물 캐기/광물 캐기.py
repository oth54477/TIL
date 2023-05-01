def solution(picks, minerals):
    global min_count
    pick_table = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    mineral_table = {"diamond":0, "iron":1, "stone":2}
    min_count = 999999999999
    L = len(minerals)

    def dfs(use_list, now, count):
        global min_count
        
        if count >= min_count:
            return

        if now >= L-1 or picks == use_list:
            min_count = min(min_count, count)
            return

        for i in range(3):
            if use_list[i] < picks[i]:
                next_now, next_count = use_pick(i, now, count)
                use_list[i] += 1
                dfs(use_list, next_now, next_count)
                use_list[i] -= 1

    def use_pick(pick_idx, now, count):
        temp = now
        for i in range(1, 6):
            if now+i < L:
                temp = now + i
                
                mineral = mineral_table[minerals[now+i]]
                count += pick_table[pick_idx][mineral]
        return temp, count

    use_list = [0, 0, 0]
    dfs(use_list, -1, 0)
    return min_count
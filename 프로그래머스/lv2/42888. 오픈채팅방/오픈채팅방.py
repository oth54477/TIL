def solution(record):
    arr = list(map(lambda x: x.split(), record))
    sort_record = sorted(arr, key=lambda x: x[1])
    chk_id = '#'
    table = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for chg in sort_record[::-1]:
        if len(chg) == 3 and chg[1] != chk_id:
            table[chg[1]] = chg[2]
            chk_id = chg[1]
    result = []
    for i in arr:
        if i[0] != 'Change':
            result.append(table[i[1]] + table[i[0]])
    return result
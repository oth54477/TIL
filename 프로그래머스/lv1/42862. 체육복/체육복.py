def solution(n, lost, reserve):
    cnt = n - len((set(lost) - set(reserve)))
    reserve, lost = set(reserve) - set(lost), set(lost) - set(reserve)
    result = set()
    for i in lost:
        if 1< i <= n and i-1 in reserve:
            result.add(i-1)
        if 0 < i <n and i+1 in reserve:
            result.add(i + 1)
    c = len(result)
    if c >= len(lost):
        cc = len(lost)
    else:
        cc = c
    answer = cnt + cc


    return answer
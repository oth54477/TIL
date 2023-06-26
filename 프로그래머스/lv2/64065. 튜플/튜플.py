def solution(s):
    s = s[2:-2]
    # 원소의 개수를 기준으로 정렬
    arr = sorted(
        list(map(lambda x: set(x.split(",")), s.split("},{"))), key=lambda x: len(x)
    )
    old_v = arr[0]
    result = [list(old_v)[0]]

    for v in arr[1:]:
        now_v = v - old_v
        result += list(now_v)
        old_v = v

    return list(map(int, result))
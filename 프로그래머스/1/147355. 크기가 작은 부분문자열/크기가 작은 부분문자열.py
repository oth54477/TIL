def solution(t, p):
    l = len(p)
    int_p = int(p)
    window = t[:l]
    result = 0
    if int(window) <= int_p:
        result += 1
    for s in t[l:]:
        window = window[1:] + s
        if int(window) <= int_p:
            result += 1
    return result
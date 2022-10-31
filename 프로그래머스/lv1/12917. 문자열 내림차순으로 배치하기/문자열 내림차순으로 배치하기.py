def solution(s):
    s = list(map(ord, s))
    s = ''.join(list(map(chr, sorted(s, reverse=True))))
    return s
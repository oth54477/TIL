def solution(s):
    l = len(s)
    ll = len(s) // 2
    if l % 2 == 0:
        return s[ll-1:ll+1]
    else:
        return s[ll]

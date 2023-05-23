def solution(n):
    m,count,result, old_m = 1, 0, 0, 1
    while m <= n+1:
        if count > n:
            while count > n:
                count -= old_m
                old_m += 1
        if count == n:
            result += 1
        count += m
        m += 1
    return result
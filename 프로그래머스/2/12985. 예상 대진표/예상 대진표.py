def solution(n,a,b):
    answer = 0
    for i in range(1, 21):
        if 2 ** i == n:
            answer = i
            break

    s, e = 1, n
    while answer > 1:
        mid = (e+s) // 2
        if a > mid and b > mid:
            s = mid+1
        elif a <= mid and b <= mid:
            e = mid
        else:
            break
        answer -= 1

    return answer
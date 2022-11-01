def solution(s):
    cnt = 0
    result = ''
    for i, v in enumerate(s):
        if v == ' ':
            cnt = 0
            result += ' '
        else:
            if cnt % 2 == 0:
                result +=  v.upper()
            else:
                result +=  v.lower()
            cnt += 1
    return result
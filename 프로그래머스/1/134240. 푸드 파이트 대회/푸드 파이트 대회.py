def solution(food):
    answer = ''
    temp = ''
    cnt = 1
    for f in food[1:]:
        temp += str(cnt) * (f//2)
        cnt += 1
    answer = temp + "0" + temp[::-1]
    return answer
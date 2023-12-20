def solution(people, limit):
    from collections import deque
    answer = 0
    people.sort()
    dq = deque(people)

    while dq:
        q1 = dq.pop()
        if dq and dq[0] <= limit - q1:
            dq.popleft()
        answer += 1

    return answer
from collections import deque

def solution(queue1, queue2):
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    s1 = sum(dq1)
    s2 = sum(dq2)
    total = s1 + s2
    count = 0
    l = len(dq1) * 3
    while count <= l:
        if s1 == s2:
            break
        elif s1 > s2:
            temp1 = dq1.popleft()
            dq2.append(temp1)
            s1 -= temp1
            s2 += temp1
        else:
            temp2 = dq2.popleft()
            dq1.append(temp2)
            s1 += temp2
            s2 -= temp2
        count += 1
    else:
        count = -1
    
    return count
def solution(k, tangerine):
    answer = 0
    from collections import Counter
    counter = Counter(tangerine)
    
    arr = sorted(counter.items(), reverse=True, key=lambda x: x[1])
    for i in arr:
        if k <= 0:
            return answer
        k -= i[1]
        answer += 1
    return answer
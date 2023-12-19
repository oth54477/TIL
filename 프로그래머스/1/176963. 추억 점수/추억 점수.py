def solution(name, yearning, photo):
    from collections import defaultdict
    answer = []
    table = defaultdict(int)
    for i, v in enumerate(name):
        table[v] = yearning[i]
    for arr in photo:
        answer.append(0)
        for i in arr:
            answer[-1] += table[i]
    return answer
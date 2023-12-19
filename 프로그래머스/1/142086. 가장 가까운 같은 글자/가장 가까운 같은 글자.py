def solution(s):
    table = dict()
    result = []
    for i, v in enumerate(s):
        if v in table:
            result.append(i-table[v])
        else:
            result.append(-1)
        table[v] = i
    return result
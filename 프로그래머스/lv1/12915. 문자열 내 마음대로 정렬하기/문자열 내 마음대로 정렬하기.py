def solution(strings, n):
    return [sorted([(ord(i[n]), i) for i in strings])[j][1] for j in range(len(strings))]